 def prepare_instance_dict(instance):
 	try:

 		for region, inst in instance.iteritems():
 			for box,price in inst.iteritems():
 				if box == 'large':
 					instance[region][box] = (price , 1)
 				if box == 'xlarge':
 					instance[region][box] = (price , 2)
 				if box == '2xlarge':
 					instance[region][box] = (price , 4)
 				if box == '4xlarge':
 					instance[region][box] = (price , 8)
 				if box == '8xlarge':
 					instance[region][box] = (price , 16)
 				if box == '10xlarge':
 					instance[region][box] = (price , 32)
 		return instance
 	except:
 		raise "Invalid instance"
 def get_min_cost(instance):
 	
 def get_costs(instances=None, hours=None, cpus=None, price=None):
 	if instances:
 		return "Instance data not available"
 	if hours or cpus or price:
 		return "Invalid request"
 	instances = prepare_instance_dict(instances)
