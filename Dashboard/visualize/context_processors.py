import requests
from collections import OrderedDict
from django.utils.html import escape
from django.utils.safestring import mark_safe
    
def get_data(request):

    api_url = 'http://127.0.0.1:8000//api/mymodels/'
    response = requests.get(api_url)
    if response.status_code == 200:
        response_data = response.json()

        form = get_filter(response_data)
        
        if request.GET:
            filtered_data = {}
            filtered_data = filter_data(request, api_url)
            data = visualize_data(filtered_data)
        else:
            data = visualize_data(response_data)

        context = {
            "form": form,
            "data": data,
        }
        
    return {'context':context}
        

def visualize_data(data):
    intensity_data={}
    likelihood_data={}
    relevance_data={}
    start_year_data={}
    end_year_data={}
    country_data={}
    topics_data={}
    regions_data={}

    for item in data:
        intensity_data[item['intensity']]=(intensity_data.get(item['intensity'],0))+1
        likelihood_data[item['likelihood']]=(intensity_data.get(item['likelihood'],0))+1
        relevance_data[item['relevance']]=(intensity_data.get(item['relevance'],0))+1
        if item['start_year']!='':
            start_year_data[item['start_year']]=(start_year_data.get(item['start_year'],0))+1 
        if item['end_year']!='':
            end_year_data[item['end_year']]=(end_year_data.get(item['end_year'],0))+1
        if item['country']!='':
            country_data[item['country']]=(country_data.get(item['country'],0))+1
        if item['topic']!='':
            topics_data[item['topic']]=(topics_data.get(item['topic'],0))+1
        if item['region']!='':
            regions_data[item['region'].title()]=(regions_data.get(item['region'].title(),0))+1 

    intensity = {
        "labels": list(intensity_data.keys()),
        "data": list(intensity_data.values()),
    }
    likelihood_data = OrderedDict(sorted(likelihood_data.items()))
    likelihood = {
        "labels": list(likelihood_data.keys()),
        "data": list(likelihood_data.values()),
    }
    relevance_data = OrderedDict(sorted(relevance_data.items()))
    relevance = {
        "labels": list(relevance_data.keys()),
        "data": list(relevance_data.values()),
    }
    start_year_data = OrderedDict(sorted(start_year_data.items()))
    start_year = {
        "labels": list(start_year_data.keys()),
        "data": list(start_year_data.values()),
    }
    end_year_data = OrderedDict(sorted(end_year_data.items()))
    end_year = {
        "labels": list(end_year_data.keys()),
        "data": list(end_year_data.values()),
    }
    year = {
        "start_year": start_year,
        "end_year": end_year
    }
    country = {
        "labels": list(country_data.keys()),
        "data": list(country_data.values()),
    }
    topic = {
        "labels": list(topics_data.keys()),
        "data": list(topics_data.values()),
    }
    region = {
        "labels": list(regions_data.keys()),
        "data": list(regions_data.values()),
    }

    final_data = {
        "intensity": intensity,
        "likelihood": likelihood,
        "relevance": relevance,
        "year": year,
        "country": country,
        "topic": topic,
        "region": region,
    }

    return final_data

def get_filter(data):
    sector = list(set([item["sector"] for item in data if item["sector"]!='']))
    pestle = list(set([item["pestle"] for item in data if item["pestle"]!='']))
    end_year = list(set([item["end_year"] for item in data if item["end_year"]!='']))
    topic = list(set([item["topic"] for item in data if item["topic"]!='']))
    region = list(set([item["region"].title() for item in data if item["region"].title()!='']))
    source = list(set([item["source"] for item in data if item["source"]!='']))
    country = list(set([item["country"] for item in data if item["country"]!='']))

    form = {
        "sector": sector,
        "pestle": pestle,
        "end_year": end_year,
        "topic": topic,
        "region": region,
        "source": source,
        "country": country,
    }
    for f in form:
        form[f].sort()
    return form

def filter_data(request, api_url):
    filters = ['sector','pestle','end_year','topic','region','source','country']
    params = { f:(request.GET[f]) for f in filters if request.GET[f] and request.GET[f]!='Select' }
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        filtered_data = []
        for item in data:
            flag = 1
            for key in params:
                if (item[key])!=params[key]:
                    flag = 0
                    break

            if flag!=0:
                filtered_data.append(item)
        return filtered_data