# Raithu Nestham - Alexa Skill Lambda Code
# Author: NaveenRaithu

def lambda_handler(event, context):
    # Alexa nunchi request vastadi
    request_type = event['request']['type']
    
    if request_type == "LaunchRequest":
        text = "Namaste! Nenu Raithu Nestham ni. Nenu raithulaki sahayam chestanu. Meeku em kavali? Panta salaalu, vాతావరణ సమాచారం, leka market dharalu?"
        return build_response(text)
    
    if request_type == "IntentRequest":
        intent_name = event['request']['intent']['name']
        
        if intent_name == "CropAdviceIntent":
            text = "Meeru veyyali anukunna panta peru cheppandi. Nenu best samayam, yeruvulu, mariyu neeti yajamanyam gurinchi chepta."
            return build_response(text)
            
        elif intent_name == "WeatherIntent":
            text = "Meeru unna ooru peru cheppandi. Nenu ee vారం weather forecast chepta."
            return build_response(text)
            
        elif intent_name == "MarketPriceIntent":
            text = "Ye panta market dhara kavali? Vari, mokkajonna, leka mirchi?"
            return build_response(text)
    
    return build_response("Dhanyavadamulu! Malli kaluddam.")

def build_response(text):
    return {
        "version": "1.0",
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": text
            },
            "shouldEndSession": False
        }
    }
