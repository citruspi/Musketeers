import unittest
from nose.tools import *
from musketeers import Musketeers

@raises(Exception)
def test_undefined_spec_exception():

	client = Musketeers(specs='tests')
	client.use("batmobile")

	params = {
		"name": "Bruce Wayne"
	}

	client.get("get", params=params).json()

@raises(Exception)
def test_undefined_resource_exception():

	client = Musketeers(specs='tests')
	client.use("httpbin")

	params = {
		"name": "Bruce Wayne"
	}

	client.get("pudding", params=params).json()

@raises(Exception)
def test_undefined_http_verb_exception():

	client = Musketeers(specs='tests')
	client.use("httpbin")

	params = {
		"name": "Bruce Wayne"
	}

	client.process("pudding", "get", params=params).json()	

@raises(Exception)
def test_missing_required_parameter_exception():

	client = Musketeers(specs='tests')
	client.use("httpbin")

	params = {
		"name": "Bruce Wayne"
	}

	client.get("get", params=params).json()

def test_get_verb():

	client = Musketeers(specs='tests')
	client.use("httpbin")

	params = {
		"name": "Bruce Wayne",
		"age": 18
	}

	response = client.get("get", params=params).json()

	assert(response['args']['name'] == "Bruce Wayne")

def test_post_verb():

	client = Musketeers(specs='tests')
	client.use("httpbin")

	form = {
		"name": "Bruce Wayne",
		"age": 18
	}

	response = client.post("post", form=form).json()

	assert(response['form']['name'] == "Bruce Wayne")

def test_direct_process_call():

	client = Musketeers(specs='tests')
	client.use('httpbin')

	form = {
		"name": "Bruce Wayne",
		"age": 18
	}

	response = client.post("post", form=form).json()

	assert(response['form']['name'] == "Bruce Wayne")