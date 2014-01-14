# musketeers.py
#
# The MIT License (MIT)
#
# Copyright (c) 2014 Mihir Singh (me@mihirsingh.com)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

try:

	import json
	import os
	import requests

except ImportError as e:

	raise Exception(e)

class Musketeers (object):

	def __init__ (self, verifySSL = None, specs='.musketeers'):

		self.verifySSL = verifySSL
		self.specs_dir = specs

	def use (self, spec):

		if os.path.exists(self.specs_dir + '/' + spec + '.json'):

			self.active_spec = spec

		else:

			raise Exception("Specification '" + self.specs_dir + "/" + spec + "' missing")

	def process (self, method, path, params, form, files, headers, spec):

		try:

			with open('/'.join([self.specs_dir, spec])+'.json', 'r') as spec:

				definition = json.loads(spec.read())
				resource = None

				for r in definition['resources']:

					if r['path'] == path:

						resource = r
						break

				if resource is None:

					raise Exception('No resource defined for path \'%s.\'' % (path))					

				if method not in resource['methods']:

					raise Exception('Path %s does not allow verb %s' % (path, method))

				for parameter in resource['params']:

					if resource['params'][parameter] == "required" and parameter not in params:

						raise Exception('Required parameter \'%s\' not defined.' % (parameter))

				if self.verifySSL is None and 'verify_ssl' not in definition:

					verifySSL = True

				elif self.verifySSL is None and 'verify_ssl' in definition:

					verifySSL = definition['verify_ssl']

				else:

					verifySSL = self.verifySSL					

				return getattr(requests, method)('/'.join([definition['api_root'], path]),
											     params=params,
											     data=form,
											     files = files,
											     headers = headers,
											     verify = verifySSL)
				
		except IOError:

			raise Exception("Specification '" + self.specs_dir + "/" + spec + "' missing")

	def get (self, path, params=None, form=None, files=None, headers=None, spec=None):

		if spec is None:

			spec = self.active_spec

		return self.process('get', path, params, form, files, headers, spec)

	def options (self, path, params=None, form=None, files=None, headers=None, spec=None):

		if spec is None:

			spec = self.active_spec

		return self.process('options', path, params, form, files, headers, spec)		

	def head (self, path, params=None, form=None, files=None, headers=None, spec=None):

		if spec is None:

			spec = self.active_spec

		return self.process('head', path, params, form, files, headers, spec)		

	def post (self, path, params=None, form=None, files=None, headers=None, spec=None):

		if spec is None:

			spec = self.active_spec

		return self.process('post', path, params, form, files, headers, spec)

	def put (self, path, params=None, form=None, files=None, headers=None, spec=None):

		if spec is None:

			spec = self.active_spec

		return self.process('put', path, params, form, files, headers, spec)

	def patch (self, path, params=None, form=None, files=None, headers=None, spec=None):

		if spec is None:

			spec = self.active_spec

		return self.process('put', path, params, form, files, headers, spec)		

	def delete (self, path, params=None, form=None, files=None, headers=None, spec=None):

		if spec is None:

			spec = self.active_spec

		return self.process('delete', path, params, spec)						