import unittest
from musketeers import Musketeers

def test_get_verb():

	client = Musketeers(specs='tests')
	client.use("httpbin")

	params = {
		"name": "Bruce Wayne",
		"age": 18
	}

	response = client.post("post", params=params).json()

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

if __name__ == "__main__":

	test_post_verb()
	test_get_verb()