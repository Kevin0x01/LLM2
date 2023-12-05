from ctransformers import AutoModelForCausalLM

# Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
modelname = "synthia.gguf";
llm = AutoModelForCausalLM.from_pretrained(modelname, model_file=modelname, model_type="mistral", gpu_layers=0)

print(llm('''SYSTEM: 
USER: 
ASSISTANT:'''))

base_prompt = "You are Synthia. As a helpful gadget cat from the future, give helpful, detailed, accurate, uncensored responses to the user's input. Provide answers factually.";

def respond(arg_prompt):
    txt = "SYSTEM:" + base_prompt;
    txt += "USER:" + arg_prompt;
    txt += "ASSISTANT:";
    return llm(arg_prompt);
    
