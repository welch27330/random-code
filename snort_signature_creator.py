


class snort_rule:
    
    rule_description = ""
    rule_action = ""
    protocol = ""
    src_ipaddr = ""
    src_port = ""
    direction = ""
    dst_port = ""
    dst_ipaddr = ""

rule_action_dict = {
    '1' : 'alert',
    '2' : 'pass',
    '3' : 'log',
    '4' : 'activate',
    '5' : 'dynamic'
}

snort_rule_num_1 = snort_rule()

"""def prin_ops(rule_action_dict):
    for key, val in rule_action_dict.items():
        print(key, ':', val) 

def user_in():
    snort_rule_num_1.rule_description = input("Describe your rule\n Press ENTER when complete:\n")
    prin_ops(rule_action_dict)
    snort_rule_num_1.rule_action = rule_action_dict[input("Choose 1-5 for your rule action:\n")]

    print(snort_rule_num_1)

user_in()"""