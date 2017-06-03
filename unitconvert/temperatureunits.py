# def convert_temperature(dec_space, amt, conv_from, conv_to):
#     temp_units = {
#         'F': {
#             'C': (amt - 32.0) * 5 / 9,
#             'K': (amt + 459.67) * 5 / 9,
#             'F': amt
#         },
#         'C': {
#             'F': (amt * 9) / 5 + 32.0,
#             'K': amt + 273.15,
#             'C': amt
#         },
#         'K': {
#             'F': amt * 9 / 5 - 459.67,
#             'C': amt - 273.15,
#             'K': amt
#         }
#     }
#     calc = round(temp_units[conv_from][conv_to], dec_space)
#     return '{0}{1} = {2}{3}'.format(amt, conv_from, calc, conv_to)

# if args.unit_from and args.unit_to in temperature:
#     print convert_temperature(4, float(args.amount), args.unit_from, args.unit_to)
