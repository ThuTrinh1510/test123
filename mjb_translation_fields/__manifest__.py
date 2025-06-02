{  
    "name": "Translation Fields",  
    "author": "Majorbird",  
    "version": "17.0.0.1",
    "category": "Hidden/Tools",
    "summary": "The module makes language translations in the Odoo system more efficient and user-friendly. The module adds the ability to view and edit the translations of a field in multiple languages, all from the same form view, simultaneously",  
    "website": "https://majorbird.cn",
    "price": 50,
    "currency": 'USD',
    "depends": [  
        'base',  
        'base_automation'
        ],  
    "data": [
        'security/ir.model.access.csv',
        'data/auto_action_translation_fields.xml',
        'views/mjb_translation_field_view.xml',
        ],  
    "_documentation": {  
        "banner": "banner.png",
        "icon": "icon.png",  
        "excerpt": "This module allows you to update values from newly created fields with specific languages into the translations of the same field and vice versa.",  
        "summary": "The 'Translation Fields' Module by Majorbird, part of the Technical category, is designed to make language translations in the Odoo system more efficient and user-friendly. The module extends the capabilities of the base Odoo system, adding the ability to view and edit the translations of a field in multiple languages, all from the same form view, simultaneously. This eliminates the need to navigate through pop-ups to edit translations. The module includes an 'updating action' feature which, when active, automatically applies updates made to a field to its corresponding translations. A 'prompt message' feature notifies users if a field hasn't been created yet, avoiding errors in data entry. Overall, this module adds a vital layer of convenience and efficiency to the linguistic element of inventory management using the Odoo system.",  
        "issue": "Users may want to view and edit the translations of a specific field in different languages on the same form view, without accessing a separate pop-up window for each language's translation.",  
        "solution": "This module introduces a checking rule for any newly created field. If the field exists, a translation action is created to allow for updating the translation value of that field. Additionally, the module initializes the newly created field with any available translation value.",  
        "manual": [  
                {  
                    "title": "Installation",  
                    "description": "The Translation Fields module can be found in the app list. To install, simply search for it and click install.",  
                    "images": ["image1.png"]  
                },  
                {  
                    "title": "Accessing the 'Translation Fields' View",  
                    "description": "Select the 'Translation Fields' submenu which can be found in the 'Translation' menu located in the Settings.",  
                    "images": ["image2.png"]  
                },  
                {  
                    "title": "Configuring Information",  
                    "description": "Complete these steps: Select 'Model', Select 'Field', Select 'Language', Toggle the active button. If a field in the specified language is created, an action is applied or a prompt message appears.",  
                    "images": ["image3.png","image4.png"]  
                },  
                {  
                    "title": "Saving Configuration and Enjoy",  
                    "description": "Please click the 'Save' button after completing your configuration then enjoy function",  
                    "images": ["image5.png","image6.png","image7.png"]  
                },  
                {  
                    "title": "Initialization",  
                    "description": "Select the field that needs to be initialized and then click the 'Initialize' button.",  
                    "images": ["image8.png","image9.png","image10.png"]  
                }  
            ],  
        "features": [  
                {  
                    "title": "Updating Action",  
                    "description": "When the 'Active' button is toggled on, an updating action is applied for the current field."  
                },  
                {  
                    "title": "Prompt Message",  
                    "description": "If a specific field has not been created yet, a warning message will appear advising that the field has not been created yet."  
                },  
                {  
                    "title": "Initialization",  
                    "description": "This feature allows you to initialize the newly created field with the current value of the translation available."  
                }  
            ]  
        },  
    "license": "OPL-1",  
    "installable": True,  
    'images': ['static/description/banner_slide.gif']
}  
