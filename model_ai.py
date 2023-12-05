from gpt4all import GPT4All

class Model():
    def __init__(self):
        self.model = GPT4All("mistral-7b-instruct-v0.1.Q4_0.gguf", allow_download=True);
        self.max_tokens = 9999;
        self.temp = 0.7;
        self.top_k = 255;
        self.top_p = 0.4;
        self.repeat_penalty = 1.18;
        self.repeat_last_n = 64;
        self.n_batch=8;
        self.system_template = ""
        self.prompt_template = "USER: {0}\nASSISTANT: ";
        
        sample = "You are a friendly assistant named Mistral.";
        
        self.system_template = sample;
        
        
        
    def respond(self, arg_prompt):
        prompt = arg_prompt;
        model = self.model;
        with model.chat_session(self.system_template, self.prompt_template):
            response = model.generate(prompt, 
            max_tokens=self.max_tokens, 
            temp=self.temp, 
            top_k=self.top_k, 
            top_p=self.top_p, 
            repeat_penalty=self.repeat_penalty, 
            repeat_last_n=self.repeat_last_n, 
            n_batch=16, 
            n_predict=None, 
            streaming=False,
            );
        return response;
        