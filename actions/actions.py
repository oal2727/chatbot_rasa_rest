# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
from typing import Dict, List, Text, Any
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from access_drive import AccessDrive


ad = AccessDrive()

# data_planes=[]
class ActionPlanDetalle(Action):

    def name(self) -> Text:
        return "action_plan_detalle" # agregar al dominio

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        plan = next(tracker.get_latest_entity_values("plan"), None)
        if  1 <= int(plan) <= 13:
            id_data = "1e_X0EDRha5_cegrHyPFptrKRHmrgenr8m7nQPOMliGk" # descuentos
            ad.get_detail_second_requerimient(dispatcher,plan,id_data)
        else:
            dispatcher.utter_message(text="El plan seleccionado no es correcto el intervalo de plan es de 1 al 13")
        return  []



class ActionMostrarDescuentos(Action):
    def name(self):
        return "action_mostrar_promociones"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        id_data = "1e_X0EDRha5_cegrHyPFptrKRHmrgenr8m7nQPOMliGk" # descuentos
        ad.get_second_requeriment(dispatcher,id_data)
        return []
