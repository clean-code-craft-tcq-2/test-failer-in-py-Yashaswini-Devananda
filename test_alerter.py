import alerter
stub_control_ok = True

def network_alert_stub(celcius):
    print(f'Stub ALERT: Temperature is {celcius} celcius')
    # Return 200 for ok
    # Return 500 for not-ok
    if stub_control_ok == True:
        return 200
    else:
        return 500 
     
alerter.alert_in_celcius(400.5)
alerter.alert_in_celcius(303.6)
print(f'{alerter.alert_failure_count} alerts failed.')
print('All is well (maybe!)')
assert(alerter.alert_failure_count == 2) 

stub_control_ok = False
alerter.alert_in_celcius(400.5)
alerter.alert_in_celcius(303.6)
print(f'{alerter.alert_failure_count} alerts failed.')
print('All is well (maybe!)')
assert(alerter.alert_failure_count == 2) 
  
