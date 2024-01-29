import pickle
import json

pvRange = 12

def API(args):
	output = {}
	f = open('data.pickle', 'rb')
	if args['mode'] in ['production', 'irradiation']:
		p = int(args['plant'])
		if 0 < p < pvRange + 1:
			d = pickle.load(f)
			cts = args['timestamp'][0:pvRange + 1].replace('T', '-')
			if cts in d['scan']:
				if args['mode'] == 'irradiation':
					output['irradiation'] = d['scan'][cts][p - 1]
				if args['mode'] == 'production':
					output['production'] = d['scan'][cts][p + pvRange - 1]
			else: raise ValueError('Invalid timestamp')
		else: raise ValueError('Invalid plant')
	elif args['mode'] == '2x-production':
		d = pickle.load(f)
		if args['plant'] in d['2x-production']:
			if args['timestamp'] in d['2x-production'][args['plant']]:
				output['production'] = d['2x-production'][args['plant']][args['timestamp']]
			else: raise ValueError('Invalid timestamp')
		else: raise ValueError('Invalid plant')
	else: raise ValueError('Invalid mode')
	return json.dumps(output)

