import os
from ..main import app,client
from .sub.helper import post_jira_issue
from requests import request
from requests.auth import HTTPBasicAuth
import requests,json

from ie_slack_bot.ie_slack_bot.sub import helper

@app.route('/sidequests', methods = ['POST' ])
def sidequests() :
    form_data = request.form
    print(form_data)

    trigger_id = form_data.get("trigger_id")
    client.chat_postMessage(channel='C087F3YFL15', text='Primeiro comando: Slash command')

    view_payload = {
        "type": "modal",
        "callback_id": "example_modal",
        "title": {"type": "plain_text", "text": "Criação de Sidequests"},
	"submit": {
		"type": "plain_text",
		"text": "Submit",
		"emoji": True
	},
	"close": {
		"type": "plain_text",
		"text": "Cancel",
		"emoji": True
	},
	"blocks": [
		{
			"type": "context",
			"elements": [
				{
					"type": "plain_text",
					"text": "------------------------------------",
					"emoji": True
				}
			]
		},
		{
			"type": "input",
			"element": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Selecione o tipo",
					"emoji": True
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "[BOTECO] | Boteco",
							"emoji": True
						},
						"value": "value-0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "[SC] | Senseconnect",
							"emoji": True
						},
						"value": "value-1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "[SQ] | Sidequest",
							"emoji": True
						},
						"value": "value-2"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "[PL] | PL",
							"emoji": True
						},
						"value": "value-3"
					}
				],
				"action_id": "static_select-action"
			},
			"label": {
				"type": "plain_text",
				"text": "CRIAÇÃO DE SIDEQUEST'S - [BOTECO, SC, SQ, PL]",
				"emoji": True
			}
		},
		{
			"type": "input",
			"element": {
				"type": "plain_text_input",
				"action_id": "plain_text_input-action"
			},
			"label": {
				"type": "plain_text",
				"text": "Informações da Solicitação",
				"emoji": True
			}
		},
		{
			"type": "input",
			"element": {
				"type": "plain_text_input",
				"action_id": "plain_text_input-action"
			},
			"label": {
				"type": "plain_text",
				"text": " ",
				"emoji": True
			}
		},
		{
			"type": "input",
			"element": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Ambiente",
					"emoji": True
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "Onboarding",
							"emoji": True
						},
						"value": "value-0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Homologação",
							"emoji": True
						},
						"value": "value-1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Produção",
							"emoji": True
						},
						"value": "value-2"
					}
				],
				"action_id": "static_select-action"
			},
			"label": {
				"type": "plain_text",
				"text": "Estrutura:",
				"emoji": True
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "users_select",
					"placeholder": {
						"type": "plain_text",
						"text": "Relator/criador",
						"emoji": True
					},
					"initial_user": " ",
					"action_id": "actionId-1"
				},
				{
					"type": "channels_select",
					"placeholder": {
						"type": "plain_text",
						"text": "Selecione o cliente:",
						"emoji": True
					},
					"initial_channel": " ",
					"action_id": "actionId-2"
				}
			]
		}
	]
}
    #modal
    response = client.views_open(trigger_id=trigger_id, view=view_payload)
    print(response)
    client.chat_postMessage(channel='C087F3YFL15', text='Segundo comando: Modal aberto')

    return "", 200

@app.route("/eventos", methods=["POST"])
def eventos():
    # Verifica o tipo de conteúdo
    if request.content_type == "application/x-www-form-urlencoded":
        payload = request.form.to_dict() # Extrair payload de form-urlencoded
        payload_string = request.form.get('payload', '')
        payload = json.loads(payload_string)
        event_type = payload.get('type')
        #client.chat_postMessage(channel='C087F3YFL15', text=f'Terceiro² comando: x-www-form-urlencoded -\n payload:{payload}\nevent_type:{event_type}')
    else:
        print(f"Tipo de conteúdo inesperado: {request.content_type} - Recebimento em application/x-www-form-urlencoded e transformado em JSON.")
        return "Unsupported Media Type", 415

    if event_type == "view_submission":
        client.chat_postMessage(channel='C087F3YFL15', text='Quarto comando: Validou application')
        #extração dos dados
        user_id = payload.get("user", {}).get("id", "unknown_user")
        state_values = payload.get("view", {}).get("state", {}).get("values",{})
        card_type = state_values.get("PFSRM",{}).get("static_select-action",{}).get("selected_option",{}).get("value","none1")
        card_branch = state_values.get("oHw2V",{}).get("static_select-action",{}).get("selected_option",{}).get("text",{}).get("text","none1")
        card_title = state_values.get("WoUC1",{}).get("plain_text_input-action",{}).get("value","none1")
        card_description = state_values.get("FPWps",{}).get("plain_text_input-action",{}).get("value","none1")
        card_relator = state_values.get("MDbhM",{}).get("actionId-1",{}).get("selected_user", None)
        card_channel = state_values.get("MDbhM",{}).get("actionId-2",{}).get("selected_channel", None)
        #transformação dos values
		
        if card_type == "value-0":
            card_type = "[BOTECO]"
        elif card_type == "value-1":
            card_type = "[SC]"
        elif card_type == "value-2":
            card_type = "[SQ]"
        elif card_type == "value-3":
            card_type = "[PL]"
        else:
            card_type = "Type not found 4command"

        card_title = card_type + " " + card_title
        client.chat_postMessage(channel='C087F3YFL15', 
                                text=f'evento: {event_type}\nuser_id:{user_id}\ncard_type:{card_type}\ncard_title:{card_title}\ncard_description:{card_description}\ncard_branch:{card_branch}\ncard_relator:{card_relator}\ncard_tenant:{card_channel}')
        card_info = f'evento: {event_type}\nuser_id:{user_id}\ncard_type:{card_type}\ncard_title:{card_title}\ncard_description:{card_description}\ncard_branch:{card_branch}\ncard_relator:{card_relator}\ncard_tenant:{card_channel}'
        jira_token = os.getenv("JIRA_TOKEN")
        jira_email = os.getenv("JIRA_EMAIL")
        jira_project = os.getenv("JIRA_PROJECT")

        url = os.getenv("JIRA_URL")
        auth = HTTPBasicAuth(jira_email, jira_token)
        """headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
        }
		
	

        jira_payload = json.dumps( {
        "fields": {
            "description": {
            "content": [
                {
                "content": [
                    {
                    "text": card_info,
                    "type": "text"
                    }
                ],
                "type": "paragraph"
                }
            ],
            "type": "doc",
            "version": 1
            },
            "labels": [
            "bugfix",
            "blitz_test"
            ],
            "issuetype": {
                "id": "10001"
            },
            "project": {
            "key": "KAN"
            },
            "summary": card_title,
        },
        "update": {}
        } )
        response = requests.request(
        "POST",
        url,
        data=jira_payload,
        headers=headers,
        auth=auth
        )
        print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))"""
        return helper.post_jira_issue(card_title, card_info,jira_project, "10001"), 200
    print(f"Evento não tratado:{event_type}")
    return "", 200
