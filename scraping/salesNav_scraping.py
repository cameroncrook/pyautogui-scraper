from bs4 import BeautifulSoup
from scraping.scraper_tools import *

def get_company_data(html):
    soup = soup = BeautifulSoup(html, 'html.parser')

    account = soup.find('div', id='account')

    img = account.find('img', attrs={'data-anonymize': 'company-logo'})
    name = account.find('div', attrs={'data-anonymize': 'company-name'})
    location = account.find('div', attrs={'data-anonymize': 'location'})
    industry = account.find('span', attrs={'data-anonymize': 'industry'})
    size = account.find('span', attrs={'data-anonymize': 'company-size'})
    revenue = account.find('span', attrs={'data-anonymize': 'revenue'})

    company_data = {
        'logo': get_attribute_value(img, 'src'),
        'name': get_text_value(name),
        'location': get_text_value(location),
        'industry': get_text_value(industry),
        'size': get_text_value(size),
        'revenue': get_text_value(revenue)
    }

    return company_data

def get_company_data_other(html):
    soup = BeautifulSoup(html, 'html.parser')

    overview = soup.find('p', class_='company-details-panel-description')

    company_info = soup.find_all('dl', 'company-details-panel__content-header')

    company_data = {
        'overview': get_text_value(overview)
    }

    for dl in company_info:
        header = dl.find('dt')
        content = dl.find('dd')

        company_data[get_text_value(header)] = get_text_value(content)

    return company_data

def get_profile_data(html):
    soup = BeautifulSoup(html, 'html.parser')

    top_card = soup.find('section', id='profile-card-section')

    img = top_card.find('img', attrs={'data-anonymize': 'headshot-photo'})
    name = top_card.find('h1', attrs={'data-anonymize': 'person-name'})
    connection_degree = name.find_next_sibling('span')
    headline = top_card.find('span', attrs={'data-anonymize': 'headline'})

    profile_data = {
        'profile_img_url': get_attribute_value(img, 'src'),
        'name': get_text_value(name),
        'connection_degree': get_text_value(connection_degree),
        'headline': get_text_value(headline),
    }

    headline_parent = headline.find_parent('div')
    general_info_parent = headline_parent.find_next_sibling('div')

    connection_address_elements = general_info_parent.find_all(recursive=False)

    profile_data['unparsed_address'] = get_text_value(connection_address_elements[0])

    for element in connection_address_elements:
        text = get_text_value(element)
        if 'shared connections' in text:
            profile_data['shared_connections'] = text
        elif 'connections' in text and ('shared' not in text):
            profile_data['connections'] = text
        else:
            profile_data['other'] = text

    city, state, country = parse_address(profile_data['unparsed_address'])
    profile_data['city'] = city
    profile_data['state'] = state
    profile_data['country'] = country

    contact_element = top_card.find('address')
    contact_li = contact_element.find_all('li')

    contact = []
    for li in contact_li:
        contact.append(get_text_value(li))

    profile_data['contact'] = contact

    about_section = soup.find('section', id='about-section')
    about = about_section.find('p')

    profile_data['about'] = get_text_value(about)

    experience_section = soup.find(id='experience-section')
    sections = experience_section.find_all('section', recursive=False)

    for section in sections:
        headline = section.find('h2').text

        if 'experience' in headline:
            experience = []
            experience_ul = section.find('ul')
            experience_li = experience_ul.find_all('li', recursive=False)

            for li in experience_li:
                info_div = li.find('div')

                company_link = info_div.find('a')
                title = info_div.find('h2', attrs={'data-anonymize': 'job-title'})
                company_name = info_div.find('p', attrs={'data-anonymize': 'company-name'})

                duration_span = info_div.find('span')
                duration = duration_span.find_parent('p')

                experience_data = {
                    'company_url': get_attribute_value(company_link, 'href'),
                    'role': get_text_value(title),
                    'company': get_text_value(company_name),
                    'duration': get_text_value(duration)
                }

                experience.append(experience_data)

            profile_data['experience'] = experience

        elif 'Education' in headline:
            education = []

            education_ul = section.find('ul')
            education_li = education_ul.find_all('li', recursive=False)

            for li in education_li:
                school_link = li.find('a')
                school = li.find('h3')
                degree = li.find('span')

                education_data = {
                    'school_url': get_attribute_value(school_link, 'href'),
                    'school': get_text_value(school),
                    'degree': get_text_value(degree)
                }

                education.append(education_data)

            profile_data['education'] = education

    return profile_data

def get_message_data(html):
    soup = BeautifulSoup(html, 'html.parser')

    message_data = []

    message_li = soup.find_all('li', class_='conversation-list-item')

    for li in message_li:
        img = li.find('img', attrs={'data-anonymize': 'headshot-photo'})
        name = li.find('div', attrs={'data-anonymize': 'person-name'})
        last_message_timestamp = li.find('time', class_='conversation-list-item__timestamp')
        
        individual_data = {
            'img_url': get_attribute_value(img, 'src'),
            'name': get_text_value(name),
            'last_message_timestamp': get_text_value(last_message_timestamp)
        }

        message_data.append(individual_data)

    return message_data

def get_thread_data(html):
    soup = BeautifulSoup(html, 'html.parser')

    thread_data = []

    thread_container = soup.find('section', class_='thread-container')
    thread_parent = thread_container.find('section', recursive=False)

    message_ul = thread_parent.find('ul')
    message_li = message_ul.find_all('li', recursive=False)

    date = None
    for li in message_li:
        date_element = li.find('div', class_='message-item__date-boundary')
        if date_element != None:
            date = date_element.find('time')
            date = get_text_value(date)

        article = li.find('article')

        if article != None:
            name_parent = li.find('address')
            name = name_parent.find('span')

            time = article.find('time')

            message = article.find('p')

            message_data = {
                'sender-name': get_text_value(name),
                'date': date,
                'time': get_text_value(time),
                'message': get_text_value(message)
            }

            thread_data.append(message_data)

    return thread_data

def get_lead_data(html):
    soup = BeautifulSoup(html, 'html.parser')

    lead_data = []

    lead_results = soup.find('ol', class_='artdeco-list')
    individuals_list = lead_results.find_all('li', class_='artdeco-list__item', recursive=False)

    for individual in individuals_list:
        profile_link_element = individual.find('a', attrs={'data-control-name': "view_lead_panel_via_search_lead_image"})

        profile_img = profile_link_element.find('img')

        name = individual.find('div', class_='artdeco-entity-lockup__title')
        connection_degree = individual.find('span', class_='artdeco-entity-lockup__degree')

        title = individual.find('span', attrs={'data-anonymize': 'title'})

        company = individual.find('a', attrs={'data-anonymize': 'company-name'})
        company_url = get_attribute_value(company, 'href')
        if company == None:
            company = individual.find('div', class_='artdeco-entity-lockup__subtitle')

        location = individual.find('span', attrs={'data-anonymize': 'location'})

        job_duration = individual.find('div', attrs={'data-anonymize': 'job-title'})

        title_duration = None
        company_duration = None

        if job_duration != None:
            job_duration_split = get_text_value(job_duration).split('  ')
        
            for duration in job_duration_split:
                if 'role' in duration:
                    title_duration = duration
                elif 'company' in duration:
                    company_duration = duration

        about = individual.find('dd')

        profile_data = {
            'profile_url': get_attribute_value(profile_link_element, 'href'),
            'img_url': get_attribute_value(profile_img, 'src'),
            'name': get_text_value(name, options=['strip']),
            'connection': get_text_value(connection_degree, options=['strip']),
            'title': get_text_value(title),
            'company_name': get_text_value(company, options=['strip'], replace=get_text_value(title)),
            'company_url': company_url,
            'unparsed_location': get_text_value(location),
            'title_duration': title_duration,
            'company_duration': company_duration,
            'about': get_text_value(about, options=['strip'])
        }

        connections_parent = individual.find('ol')
        if connections_parent != None:
            connections_li = connections_parent.find_all('li', recursive=False)

            for li in connections_li:
                data = li.find('span').text

                if 'TeamLink' in data:
                    profile_data['teamlink_connections'] = trim_text(data)
                elif 'mutual' in data:
                    connections = trim_text(data)
                    profile_data['mutual_connections'] = get_digits(connections)
                elif 'Linkedin' in data:
                    profile_data['activity'] = trim_text(data)
                else:
                    profile_data['other'] = trim_text(data)

        city, state, country = parse_address(profile_data['unparsed_location'])
        profile_data['city'] = city
        profile_data['state'] = state
        profile_data['country'] = country

        lead_data.append(profile_data)

    return lead_data