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
    content = soup.find('main', {'id': 'content'}).find('div', {'id': 'bodyContent'}).find('div',
                                                                                           {'id': 'mw-content-text'})
    patrol_named = ['First patrol', 'Second patrol', 'Third patrol', 'Fourth patrol', 'Fifth patrol', 'Sixth patrol',
                    'Seventh patrol', 'Eighth patrol', 'Ninth patrol', 'Tenth patrol', 'Eleventh patrol',
                    'Twelfth patrol', 'First patrol and loss', 'Second patrol and loss', 'Third patrol and loss',
                    'Fourth patrol and loss', 'Fifth patrol and loss', 'Sixth patrol and loss',
                    'Seventh patrol and loss', 'Eighth patrol and loss', 'Ninth patrol and loss',
                    'Tenth patrol and loss', 'Eleventh patrol and loss',
                    'Twelfth patrol and loss']
    double_patrols = ['First and second patrols', 'Second and third patrols', 'Third and fourth patrols',
                      'Fourth and fifth patrols', 'Fifth and sixth patrols', 'Sixth and seventh patrols',
                      'Seventh and eighth patrols', 'Eighth and ninth patrols', 'Ninth and tenth patrols',
                      'Tenth and eleventh patrols', 'Eleventh and twelfth patrols']
    patrols = 0
    all_lv3 = content.find_all('div', {'class': 'mw-heading mw-heading3'})
    for lv3 in all_lv3:
        if lv3.text.replace('[edit]', '') in patrol_named:
            patrols += 1
        elif lv3.text.replace('[edit]', '') in double_patrols:
            patrols += 2
    return patrols


# get the wolfpacks the boat was in and the dates
def get_wolfpack_data(soup):
    content = soup.find('main', {'id': 'content'}).find('div', {'id': 'bodyContent'}).find('div',
                                                                                           {'id': 'mw-content-text'})
    wolfpacks = content.find('h3', id='Wolfpacks')
    if not wolfpacks:
        return None
    wolfpack_list = wolfpacks.find_next('ul').text
    wolfpacks_list = wolfpack_list.split('\n')
    wolfpack_dict = {}
    for wp in wolfpacks_list:
        pack = wp[:wp.find('(')].strip()
        dates = wp[wp.find('(') + 1:wp.find(')')].split('–')
        dates = [x.strip() for x in dates]
        wolfpack_dict[pack] = dates
    return wolfpack_dict


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
    i = 0
    for row in cleaned:
        if 'Flotilla' in row:
            try:
                split_dates = cleaned[i + 1].split('–')

                cleaned_dict[row] = split_dates

            except Exception as e:
                print(f"Error processing row: {row}, error: {e}")
        i += 1
    return cleaned_dict


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
        patrols = get_patrol_count(boat_soup)
        wolfpacks = get_wolfpack_data(boat_soup)
        flotilla = get_floatilla_data(boat_soup)

        data.append(
            [name, year, type_, cmd_of_note, warships_sunk_n_total_loss_no, warships_sunk_n_total_loss_tons_n_grt,
             warships_damaged_no, warships_damaged_tons_n_grt, merchant_ships_sunk_no, merchant_ships_sunk_grt,
             merchant_ships_damaged_no, merchant_ships_damaged_grt, merchant_ships_total_loss_no,
             merchant_ships_total_loss_grt, fate_event, fate_date, notes, url, commissioned, patrols, wolfpacks,
             flotilla])
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
                                 'Fate_Date', 'Notes', 'URL', 'Commissioned', 'Patrols', 'Wolfpacks', 'Flotilla'])
# drop \n from everywhere
df = df.replace('\n', '', regex=True)
df.to_csv('uboats.csv', index=False)
