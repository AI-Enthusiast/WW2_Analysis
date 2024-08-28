import pandas as pd  # pip3 install pandas
import os
import requests
import bs4 as bs  # pip3 install beautifulsoup4
from tqdm import tqdm  # pip3 install tqdm
from datetime import datetime


# get raw soup data
def get_u_boat_data(url):
    req = requests.get(url)
    soup = bs.BeautifulSoup(req.text, 'html.parser')
    # print(soup.prettify())
    return soup


# get the commission date of the boat
def get_commmissioned_date(soup):
    infobox = soup.find('table', {'class': 'infobox'})
    commissioned = infobox.find('td', string='Commissioned').find_next('td').text
    commissioned = commissioned.split('[')[0]
    # df.loc[df['URL'] == boat, 'Commissioned'] = commissioned
    # convet commissiond to date time then y-m-d, eg: 29 July 1935, 1935-07-29
    try:
        commissioned = datetime.strptime(commissioned, '%d %B %Y').strftime('%Y-%m-%d')
    except ValueError:
        commissioned = None
    return commissioned


# get the count of patrols the boat went on
def get_patrol_count(soup):
    try:
        content = soup.find('main', {'id': 'content'}).find('div', {'id': 'bodyContent'}).find('div',
                                                                                               {
                                                                                                   'id': 'mw-content-text'})
        infobox = content.find('table', {'class': 'infobox'})
        patrols = infobox.find('td', string='Operations:').find_next('td').text
        pre_count = patrols.count('patrol') - 1 if patrols.count('patrol') > 1 else patrols.count('patrol')
    except:
        return None, 0
        # patrols =
        # ('\n\n7 patrols:\n1st patrol:\n26 September – 15 December 1942\n2nd patrol:\n11 January – 27 April 1943\n3rd patrol:\n24 June – 3 July 1943\n4th patrol:\n18 August – 1 December 1943\n5th patrol:\na. 23 January – 7 May 1944\nb. 4 – 10 July 1944\n6th patrol:\na. 15 July – 24 October 1944\nb. 25 – 28 October 1944\nc. 5 – 10 March 1945\n7th patrol: 12 March – 22 April 1945\n', 7)
        patrols = patrols.replace('\n', '|').replace('||','')

        # if the first char is a digit, and the next is 'patrols:' then we are only interested in what comes after
        if patrols[0].isdigit() and 'patrols' in patrols.split(':')[0]:
            patrols = patrols.split(':')[1:]
            patrols = ':'.join(patrols)
            # '|1st patrol:|26 September – 15 December 1942|2nd patrol:|11 January – 27 April 1943|3rd patrol:|24 June – 3 July 1943|4th patrol:|18 August – 1 December 1943|5th patrol:|a. 23 January – 7 May 1944|b. 4 – 10 July 1944|6th patrol:|a. 15 July – 24 October 1944|b. 25 – 28 October 1944|c. 5 – 10 March 1945|7th patrol: 12 March – 22 April 1945|'
            # split by '|'
            patrols = patrols.split('|')
            patrols_dict = {} # patrols : [date list]
            last_patrol = None
            for i, p in enumerate(patrols):
                if 'patrol' in p:
                    print("Patrol:", p, i)
                    # check it doesn't also have a date
                    # eg 7th patrol: 12 March – 22 April 1945
                    if len(p.split(':')) == 2 and p.split(':')[1] != "":
                        split_patrol = p.split(':')
                        try:
                            prior_patrols_under_same_header = patrols_dict[split_patrol[0]]
                            patrols_dict[split_patrol[0]] =  prior_patrols_under_same_header.append(split_patrol[1])
                        except:
                            patrols_dict[split_patrol[0]] = [split_patrol[1]]
                        last_patrol = split_patrol[0]
                    else:
                        last_patrol = p
                else:
                    if last_patrol is not None:
                        print("Date:", p, i, last_patrol)
                        try:
                            prior_patrols_under_same_header = patrols_dict[last_patrol]
                            print('Prior:', prior_patrols_under_same_header)
                            prior_patrols_under_same_header.append(p)
                            patrols_dict[last_patrol] = prior_patrols_under_same_header
                        except:
                            patrols_dict[last_patrol] = [p]
                            print('First date:', p)
            patrols = patrols_dict
        else:
            patrols = patrols
    return patrols, pre_count


# get the wolfpacks the boat was in and the dates
def get_wolfpack_data(soup):
    content = soup.find('main', {'id': 'content'}).find('div', {'id': 'bodyContent'}).find('div',
                                                                                           {'id': 'mw-content-text'})
    wolfpacks = content.find('h3', id='Wolfpacks')
    if not wolfpacks:
        return None, 0
    wolfpack_list = wolfpacks.find_next('ul').text
    wolfpacks_list = wolfpack_list.split('\n')
    wolfpack_dict = {}
    wolfpack_count = 0
    for wp in wolfpacks_list:
        pack = wp[:wp.find('(')].strip()
        dates = wp[wp.find('(') + 1:wp.find(')')].split('–')
        dates = [x.strip() for x in dates]
        wolfpack_dict[pack] = dates
        wolfpack_count += 1
    return wolfpack_dict, wolfpack_count


# get the flotilla the boat was in and the dates
def get_floatilla_data(soup):
    content = soup.find('main', {'id': 'content'}).find('div', {'id': 'bodyContent'}).find('div',
                                                                                           {'id': 'mw-content-text'})
    infobox = content.find('table', {'class': 'infobox'})
    part_of = infobox.find('td', string='Part of:').find_next('td').text
    cleaned = part_of.replace('\n\n', ',').replace('\n', ',').replace('\t', '').split(',')
    cleaned = [x.strip() for x in cleaned]
    cleaned = [x for x in cleaned if x]
    cleaned_dict = {}
    flotilla_count = 0
    i = 0
    for row in cleaned:
        if 'Flotilla' in row:
            try:
                split_dates = cleaned[i + 1].split('–')

                cleaned_dict[row] = split_dates
                flotilla_count += 1
            except Exception as e:
                print(f"Error processing row: {row}, error: {e}")
        i += 1
    return cleaned_dict, flotilla_count


def get_data(soup):
    wikitable = soup.find('table', {'class': 'wikitable'})
    data = []
    for row in tqdm(wikitable.find_all('tr')[3:]):
        href = row.find_all('td')[0].find('a')['href']
        url = 'https://en.wikipedia.org' + href
        name = row.find_all('td')[0].text
        year = row.find_all('td')[1].text
        type_ = row.find_all('td')[2].text
        cmd_of_note = row.find_all('td')[3].text

        warships_sunk_n_total_loss_no = row.find_all('td')[4].text
        warships_sunk_n_total_loss_tons_n_grt = row.find_all('td')[5].text
        warships_damaged_no = row.find_all('td')[6].text
        warships_damaged_tons_n_grt = row.find_all('td')[7].text

        merchant_ships_sunk_no = row.find_all('td')[8].text
        merchant_ships_sunk_grt = row.find_all('td')[9].text
        merchant_ships_damaged_no = row.find_all('td')[10].text
        merchant_ships_damaged_grt = row.find_all('td')[11].text
        merchant_ships_total_loss_no = row.find_all('td')[12].text
        merchant_ships_total_loss_grt = row.find_all('td')[13].text

        fate_event = row.find_all('td')[14].text
        fate_date = row.find_all('td')[15].text

        notes = row.find_all('td')[16].text

        boat_soup = get_u_boat_data(url)
        commissioned = get_commmissioned_date(boat_soup)
        patrols, p_count = get_patrol_count(boat_soup)
        wolfpacks, w_count = get_wolfpack_data(boat_soup)
        flotilla, f_count = get_floatilla_data(boat_soup)

        data.append(
            [name, year, type_, cmd_of_note, warships_sunk_n_total_loss_no, warships_sunk_n_total_loss_tons_n_grt,
             warships_damaged_no, warships_damaged_tons_n_grt, merchant_ships_sunk_no, merchant_ships_sunk_grt,
             merchant_ships_damaged_no, merchant_ships_damaged_grt, merchant_ships_total_loss_no,
             merchant_ships_total_loss_grt, fate_event, fate_date, notes, url, commissioned, patrols, p_count, wolfpacks,
             w_count, flotilla, f_count])
    return data


url_1 = 'https://en.wikipedia.org/wiki/List_of_German_U-boats_in_World_War_II_(1-599)'
url_2 = 'https://en.wikipedia.org/wiki/List_of_German_U-boats_in_World_War_II_(600-4712)'
data = []
for wiki_url in [url_1, url_2]:
    soup = get_u_boat_data(wiki_url)
    data.extend(get_data(soup))

df = pd.DataFrame(data, columns=['Name', 'Year', 'Type', 'Notable Commanders', 'Warships_sunk_n_total_loss_No',
                                 'Warships_sunk_n_total_loss_Tons-n-GRT', 'Warships_Damaged_No',
                                 'Warships_Damaged_Tons-n-GRT', 'Merchant_Ships_sunk_No', 'Merchant_Ships_sunk_GRT',
                                 'Merchant_Ships_damaged_No', 'Merchant_Ships_damaged_GRT',
                                 'Merchant_Ships_total_loss_No', 'Merchant_Ships_total_loss_GRT', 'Fate_Event',
                                 'Fate_Date', 'Notes', 'URL', 'Commissioned', 'Patrols', 'Patrols_Count', 'Wolfpacks', 'Wolfpacks_Count','Flotilla', 'Flotilla_Count'])
# drop \n from everywhere
df = df.replace('\n', '', regex=True)
df.to_csv('uboats.csv', index=False)
