import xlwings as xw
wb = xw.Book('/Users/ke/Library/CloudStorage/OneDrive-КОМУС/!DayReports/12_Dec_22/Планшеты_октябрь22.xlsx')

# Указываем имя копируемого листа
var_sheet = wb.sheets['Tablets']

# Делаем копии листа выше
var_sheet.copy(name='Москва и ЦФО')
var_sheet.copy(name='РП Волгоград')
var_sheet.copy(name='РП Екатеринбург')
var_sheet.copy(name='РП Казань')
var_sheet.copy(name='РП Краснодар')
var_sheet.copy(name='РП Н.Новгород')
var_sheet.copy(name='РП Новосибирск')
var_sheet.copy(name='РП Омск')
var_sheet.copy(name='РП Пермь')
var_sheet.copy(name='РП Ростов-на-Дону')
var_sheet.copy(name='РП Самара')
var_sheet.copy(name='РП Санкт-Петербург')
var_sheet.copy(name='РП Саратов')
var_sheet.copy(name='РП Уфа')
var_sheet.copy(name='РП Челябинск')