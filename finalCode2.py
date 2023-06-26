import plotly.express as px
import db

connection = db.connect('shad112_prmetro', '1234', "91.190.239.132", "5432", "SHAD112_Pr_Metro")

def get_axises(data: classmethod) -> classmethod:
    x, y = [], []

    for value in data:
        x.append(value[0])
        y.append(value[1])
    
    return x, y

print(get_axises(db.count_validation(connection, '2020')))
#fig = px.bar(get_axises(db.count_validation(connection, '2020')))
#fig.show()
