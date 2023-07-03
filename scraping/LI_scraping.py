from bs4 import BeautifulSoup
from scraping.scraper_tools import *

#========================================================================================
# Company Scraping
#========================================================================================
def get_company_data(html):
    soup = BeautifulSoup(html, 'html.parser')

    # Gets top info
    top_parent = soup.find('div', class_='org-top-card__primary-content')
    company_name = top_parent.find('h1', class_='org-top-card-summary__title').text
    tag_line = top_parent.find('p', class_='org-top-card-summary__tagline').text
    industry_followers = top_parent.find_all('div', class_='org-top-card-summary-info-list__info-item')
    for data in industry_followers:
        data = trim_text(data.text)
        if "followers" in data:
            followers = data

    # Gets buttom info
    bottom_element = soup.find('div', class_='org-grid__content-height-enforcer')
    description = bottom_element.find('p').text
    other_info_parent = bottom_element.find('dl')
    other_info = other_info_parent.find_all(recursive=False)

    other_info_dict = {}
    for info in other_info:
        if info.name == ('dt'):
            heading = trim_text(info.text)
            other_info_dict[heading] = []
        elif info.name == ('dd'):
            other_info_dict[heading].append(trim_text(info.text))

    company_data = {
        "name": trim_text(company_name),
        "tag_line": trim_text(tag_line),
        "industry": trim_text(industry_followers[0].text),
        "followers": followers,
        "description": trim_text(description)
    }

    for key, value in other_info_dict.items():
        if len(value) > 1:
            company_data[key.lower()] = value
        else:
            company_data[key.lower()] = value[0]

    return company_data

#========================================================================================
# Profile Scraping
#========================================================================================
def get_profile_contact_data(html):
    soup = BeautifulSoup(html, 'html.parser')

def get_profile_data(html):
    soup = BeautifulSoup(html, 'html.parser')

    profile_data = {}

    # Get Contact Info
    contact_div = soup.find('div', class_='pv-profile-section__section-info')
    contact_sections = contact_div.find_all('section', class_='pv-contact-info__contact-type', recursive=False)

    for section in contact_sections:
        heading = section.find('h3').text

        if 'Profile' in heading:
            heading = 'profile_url'

        value = section.find('div', class_='pv-contact-info__ci-container').text

        profile_data[trim_text(heading).lower()] = trim_text(value)
    # contact = contact_div.find_all('a', class_='pv-contact-info__contact-link')
    # url = contact[0].text
    # email = contact[1].text

    # profile_data['url'] = trim_text(url)
    # profile_data['email'] = trim_text(email)

    # Gets data from top card
    profile_img = soup.find('img', class_='pv-top-card-profile-picture__image')
    img_src = profile_img['src']
    profile_data['profile_img'] = img_src

    name = soup.find('h1').text
    profile_data['name'] = trim_text(name)

    rank = soup.find('span', class_='dist-value').text
    profile_data['rank'] = trim_text(rank)

    subtitle = soup.find('div', class_='text-body-medium')
    if subtitle != None:
        profile_data['subtitle'] = trim_text(subtitle.text)

    location_div = soup.find_all('div', class_='pv-text-details__left-panel')
    location = location_div[1].find('span', class_='text-body-small').text
    profile_data['location'] = trim_text(location)

    connections = soup.find('span', class_='t-bold').text
    profile_data['Connections'] = trim_text(connections)

    # Gets experience, education, skills, and interests data
    main_element = soup.find('main')
    sections = main_element.find_all('section', recursive=False)
    
    for section in sections:
        heading_h2 = section.find('h2')

        if heading_h2 != None:
            heading = heading_h2.find('span').text

            if heading == 'Experience':
                experience_ul = section.find('ul', class_='pvs-list')
                experience_li = experience_ul.find_all('li', recursive=False)

                experience = []
                for experience_data in experience_li:
                    div_parent = experience_data.find('div', class_='pvs-entity')
                    div_dividors = div_parent.find_all('div', recursive=False)

                    experience_parent = div_dividors[1]

                    experience_divs = experience_parent.find_all('div', recursive=False)

                    if len(experience_divs) > 1:
                        # This is for jobs with multiple positions
                        company_url = experience_divs[0].find('a')
                        company_name = company_url.find('span')
                        duration = company_url.find('span', recursive=False)

                        job_title_ul = experience_divs[1].find('ul')
                        job_title_list = job_title_ul.find_all('li', recursive=False)

                        job_title = []
                        for job_title_li in job_title_list:
                            title = job_title_li.find('span')
                            job_title.append(get_text_value(title))

                    else:
                        # This is for jobs with 1 title
                        company_url = div_dividors[0].find('a')
                        job_title = div_dividors[1].find('span')
                        job_title = get_text_value(job_title)
                        company_duration = div_dividors[1].find_all('span', class_="t-14")
                        company_name = company_duration[0].find('span')
                        duration = company_duration[1]

                    experience_dict = {
                        "company_url": get_attribute_value(company_url, 'href'),
                        'company_name': get_text_value(company_name),
                        'job_title': job_title,
                        'duration': get_text_value(duration),
                    }

                    experience.append(experience_dict)

                    # job_title_parent = experience_data.find('span', class_='mr1 t-bold')
                    # job_title = job_title_parent.find_all('span')

                    # job_data_parent = experience_data.find('div', class_='display-flex flex-column full-width')
                    # job_data = job_data_parent.find_all('span', recursive=False)
                    # company_work = job_data[0].find('span').text
                    # company_work_split = company_work.split('·')
                    # company_name = company_work_split[0]
                    # work_type = company_work_split[1]

                    # duration_phrame = job_data[1].find('span').text
                    # duration_split = duration_phrame.split('·')

                    # # Gets Work Dates
                    # dates_split = duration_split[0].split('-')
                    # start_year = dates_split[0]
                    # end_year = dates_split[1]

                    # duration = duration_split[1]

                    # experience_dict = {
                    #     "job_title": trim_text(job_title[0].text),
                    #     'company': trim_text(company_name),
                    #     'work_type': trim_text(work_type),
                    #     'start_year': trim_text(start_year),
                    #     'end_year': trim_text(end_year),
                    #     'duration': trim_text(duration)
                    # }

                    # experience.append(experience_dict)

                profile_data['experience'] = experience
            if heading == 'Education':
                education_ul = section.find('ul', class_='pvs-list')
                education_li = education_ul.find_all('li', class_='pvs-list__item--line-separated', recursive=False)

                educations = []
                for education_data in education_li:
                    school_parent = education_data.find('div', class_='pvs-entity')
                    school_divs = school_parent.find_all('div', recursive=False)

                    school_url = school_divs[1].find('a')
                    school_name = school_divs[1].find('span')

                    degree_info = school_url.find_all('span', recursive=False)

                    if len(degree_info) > 1:
                        degree = degree_info[0].find('span')
                        duration = degree_info[1].find('span')
                    else:
                        degree = None
                        duration = degree_info[0].find('span')

                    education = {
                        'school_url': get_attribute_value(school_url, 'href'),
                        'school_name': get_text_value(school_name),
                        'degree': get_text_value(degree),
                        'duration': get_text_value(duration),
                    }

                    # school_parent = education_data.find('span', class_='mr1 hoverable-link-text t-bold')
                    # school = school_parent.find('span').text

                    # data_parent = education_data.find_all('a', class_='optional-action-target-wrapper')
                    # span_data = data_parent[1].find_all('span', recursive=False)

                    # if len(span_data) > 1:
                    #     degree = trim_text(span_data[0].find('span').text)
                    #     duration = span_data[1].find('span').text
                    # else:
                    #     degree = None
                    #     duration = span_data[0].find('span').text

                    # duration_split = duration.split('-')
                    # start_year = duration_split[0]
                    # end_year = duration_split[1]

                    # education = {
                    #     'School': trim_text(school),
                    #     'degree': degree,
                    #     'start_year': trim_text(start_year),
                    #     'end_year': trim_text(end_year)
                    # }

                    educations.append(education)
                
                profile_data['education'] = educations

    return profile_data
                    
#========================================================================================
# Connections Scraping
#========================================================================================
def get_connections_data(html):
    soup = BeautifulSoup(html, 'html.parser')

    # Handle profiles without subtitles
    total_connections = soup.find('h1').get_text(strip=True)

    connections_list = [
        {
            'Total Connections': total_connections
        }
    ]

    connections_li = soup.find_all('li', class_='mn-connection-card')
    for connection_data in connections_li:
        profile_url = connection_data.find('a', class_='mn-connection-card__link')
        title = connection_data.find('span', class_='mn-connection-card__name').get_text(strip=True)
        subtitle = connection_data.find('span', class_='mn-connection-card__occupation')
        con_time = connection_data.find('time', class_='time-badge').text

        connection = {
            'profile_url': get_attribute_value(profile_url, 'href'),
            'Title': title,
            'Subtitle': None,
            'Time': trim_text(con_time)
        }

        if subtitle != None:
            connection['Subtitle'] = subtitle.get_text(strip=True)

        connections_list.append(connection)

    return connections_list

#========================================================================================
# Invitations Scraping
#========================================================================================

def get_invitations_data(html):
    soup = BeautifulSoup(html, 'html.parser')

    invitations_ul = soup.find('ul', class_='mn-invitation-list')
    invitations_li = invitations_ul.find_all('li', class_='invitation-card', recursive=False)

    invitations_list = []
    for invitation_data in invitations_li:
        title = invitation_data.find('span', class_='invitation-card__title').text
        subtitle = invitation_data.find('span', class_='invitation-card__subtitle')
        time = invitation_data.find('time', class_='time-badge').text
        note = invitation_data.find('span', class_='lt-line-clamp__line')

        invitation = {
            'Name': trim_text(title),
            'Subtitle': None,
            'Time': trim_text(time),
            'Note': None
        }

        if subtitle != None:
            invitation['Subtitle'] = trim_text(subtitle.text)
        if note != None:
            invitation['Note'] = trim_text(note.text)

        invitations_list.append(invitation)

    return invitations_list

#========================================================================================
# Messages Scraping
#========================================================================================
def get_chats(html):
    soup = BeautifulSoup(html, 'html.parser')

    chats_ul = soup.find('ul', class_='list-style-none msg-conversations-container__conversations-list')
    
    participants = chats_ul.find_all('h3', class_='msg-conversation-card__participant-names')

    return participants

def get_thread(html):
    soup = BeautifulSoup(html, 'html.parser')

    thread_name = soup.find(id='thread-detail-jump-target').text

    message_ul = soup.find('ul', class_='msg-s-message-list-content')

    messages_li = message_ul.find_all('li', class_='msg-s-message-list__event', recursive=False)

    message_thread = []
    previous_time = ''
    order = 0
    for message_data in messages_li:
        sender = message_data.find('span', class_='msg-s-message-group__name').text
        time = message_data.find('time', class_='msg-s-message-group__timestamp').text
        note = message_data.find('p', class_='msg-s-event-listitem__body').text

        if time == previous_time:
            order += 1
        else:
            order = 0

        previous_time = time

        message = {
            'Thread': trim_text(thread_name),
            'Sender': trim_text(sender),
            'Timestamp': trim_text(time),
            'Order': order,
            'Message': trim_text(note)
        }

        message_thread.append(message)

    return message_thread