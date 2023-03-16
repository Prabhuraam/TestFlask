def handler(context, basicio):
    
    city = basicio.get_argument('name')
    context.log(f"This is the city name:{city}")
    context.log('Successfully executed basicio function')
    basicio.write(f'Hello from {city}')
    context.close()
