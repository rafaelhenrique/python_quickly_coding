# coding: utf-8
# Pega os simbolos das codificações na tupla locales
import locale

locales = (
    'pt_BR.utf8', 'en_AU.utf8', 'en_BW.utf8', 'en_CA.utf8',
    'en_DK.utf8', 'en_GB.utf8', 'en_HK.utf8', 'en_IE.utf8',
    'en_IN', 'en_NG', 'en_PH.utf8', 'en_US.utf8', 'en_ZA.utf8',
    'en_ZW.utf8', 'ja_JP.utf8')

# No setlocale o 'código' do locale tem que existir na máquina
# local
for l in locales:
    locale.setlocale(locale.LC_ALL, locales[0])
    conv = locale.localeconv()

    print(
        '{ics} ==> {s}'.format(
            ics=conv['int_curr_symbol'],
            s=conv['currency_symbol']
        )
    )
