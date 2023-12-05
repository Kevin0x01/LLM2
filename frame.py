import tkinter as tk
import model_ai as model;
    
def read_text(arg_box):
    return arg_box.get("1.0", "end-1c");

def write_text(arg_box, arg_txt):
    arg_box.insert("end", arg_txt);

def delete_text(arg_box):
    arg_box.delete("1.0", "end");
    
def submit():
    prompt = read_text();
    response = model.respond(prompt);
    write_text(output, response);
    

wnd = tk.Tk()

wnd.geometry("400x400");
wnd.resizable(False, False);
wnd.title("Synthia AI Chat")

row = 0;

lbl_intro = tk.Label(wnd, text="Chat with Synthia AI!");
lbl_intro.grid(row=row, column=0, padx=10, pady=10);

row += 1;

entry = tk.Text(wnd, width=32, height=3, wrap="word")
entry.grid(row=row, column=0, padx=10, pady=10)

submit_button = tk.Button(wnd, text="Ask", command=submit, padx=10, pady=10)
submit_button.grid(row=row, column=1)

row += 1;

lbl_resp = tk.Label(wnd, text="Synthia's Response:");
lbl_resp.grid(row=row, column=0, padx=10, pady=10);

row += 1;

output = tk.Text(wnd, width=32, height=5, wrap="word");
output.grid(row=row, column=0, columnspan=2, padx=10, pady=10)

wnd.mainloop()
