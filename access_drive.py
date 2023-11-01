from google.oauth2 import service_account
from googleapiclient.discovery import build
import gspread

class AccessDrive:
    def __init__(self):
        self.credenciales_json = 'client.json'
        self.credenciales = service_account.Credentials.from_service_account_file(
            self.credenciales_json, 
            scopes=['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/spreadsheets'] # permisos de spreadhets y drive
        )
        self.drive_service = build('drive', 'v3', credentials=self.credenciales)
        self.client = gspread.authorize(self.credenciales)
    def get_second_requeriment(self,dispatcher,id_data):
        sheet = self.client.open_by_key(id_data).sheet1 # nombre de pagina
        data = sheet.get_all_records()
        i=1
        mensaje= "\n Listado de Planes: \n"
        for row in data:
            plan = row.get('Planes')
            mensaje += f" - {i} Plan: {plan} \n"
            i+=1
        mensaje += " Indique el detalle del plan Seleccionado del 1 al 13"
        dispatcher.utter_message(mensaje)

    def get_detail_second_requerimient(self,dispatcher,selected,id_data):
        sheet = self.client.open_by_key(id_data).sheet1 # nombre de pagina
        data = sheet.get_all_records()
        i=1
        data_planes=[]
        for row in data:
            plan = row.get('Planes')
            data_planes.append(plan)

        nombre_plan = data_planes[int(selected)-1]
        plan_encontrado = list(filter(lambda x: x['Planes'] == nombre_plan, data))
        if plan_encontrado:
            plan_array = plan_encontrado[0] # acceder al objeto
            # print(plan_array.values()) dict_values(['a', 'b', 'c'])
            key_values =  list(plan_array.values()) # listar y accedera los valores y pasar a array cada valor  [planes,cargo_fijo,descuento,etc]
            plan = key_values[0]
            cargo_fijo = key_values[1] 
            descuento_3_mes = key_values[2] 
            descuento_12_mes = key_values[3] 
            mensaje = f" \n ==> Nombre de Plan {plan}\n"
            mensaje += "   - Detalle de Plan:\n"
            mensaje += f"   -Cargo Fijo: {cargo_fijo}\n"
            mensaje += f"   -Descuento 3° mes: {descuento_3_mes}\n"
            mensaje += f"   -Descuento 12° mes: {descuento_12_mes}"

            dispatcher.utter_message(mensaje)
        else:
            print(f"Plan '{nombre_plan}' no encontrado")
    def get_thrid_requeriment(self):
        pass
