import tkinter as tk
from tkinter import filedialog, messagebox
import os

root = tk.Tk()
root.title("FFmpeg GUI")

# Input file selection
def browse_input_file():
    input_file = filedialog.askopenfilename(title="Select input file", filetypes=[("All files", "*.*")])
    input_file_path.set(input_file)

input_file_label = tk.Label(root, text="Input file:")
input_file_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
input_file_path = tk.StringVar()
input_file_entry = tk.Entry(root, textvariable=input_file_path, width=50)
input_file_entry.grid(row=1, column=0, padx=10)
browse_input_button = tk.Button(root, text="Browse", command=browse_input_file)
browse_input_button.grid(row=1, column=1)

# Output folder selection
def browse_output_folder():
    output_folder = filedialog.askdirectory(title="Select output folder")
    output_folder_path.set(output_folder)

output_folder_label = tk.Label(root, text="Output folder:")
output_folder_label.grid(row=2, column=0, sticky="w", padx=10, pady=10)
output_folder_path = tk.StringVar()
output_folder_entry = tk.Entry(root, textvariable=output_folder_path, width=50)
output_folder_entry.grid(row=3, column=0, padx=10)
browse_output_button = tk.Button(root, text="Browse", command=browse_output_folder)
browse_output_button.grid(row=3, column=1)

# Output file name and codecs selection
output_file_label = tk.Label(root, text="Output file name:")
output_file_label.grid(row=4, column=0, sticky="w", padx=10, pady=10)
output_file_name = tk.Entry(root, width=50)
output_file_name.grid(row=5, column=0, padx=10)

video_codec_label = tk.Label(root, text="Video codec:")
video_codec_label.grid(row=6, column=0, sticky="w", padx=10, pady=10)
video_codecs = ["h264", "hevc", "vp9"]
video_codec = tk.StringVar()
video_codec.set(video_codecs[0])
video_codec_dropdown = tk.OptionMenu(root, video_codec, *video_codecs)
video_codec_dropdown.grid(row=7, column=0, padx=10)

audio_codec_label = tk.Label(root, text="Audio codec:")
audio_codec_label.grid(row=6, column=1, sticky="w", padx=10, pady=10)
audio_codecs = ["aac", "mp3", "opus"]
audio_codec = tk.StringVar()
audio_codec.set(audio_codecs[0])
audio_codec_dropdown = tk.OptionMenu(root, audio_codec, *audio_codecs)
audio_codec_dropdown.grid(row=7, column=1, padx=10)

# Use NVENC checkbox
nvenc_checkbox_var = tk.BooleanVar()
nvenc_checkbox = tk.Checkbutton(root, text="Use NVENC", variable=nvenc_checkbox_var)
nvenc_checkbox.grid(row=8, column=0, sticky="w", padx=10, pady=10)

# FFmpeg command execution
def run_ffmpeg():
    input_file = input_file_path.get()
    output_folder = output_folder_path.get()
    output_file = os.path.join(output_folder, output_file_name.get())

    video_codec_selection = "-c:v " + video_codec.get()
    audio_codec_selection = "-c:a " + audio_codec.get()
    
    if nvenc_checkbox_var.get():
        video_codec_selection += " -c:v h264_nvenc"
        
    ffmpeg_command = f"ffmpeg -i \"{input_file}\" {video_codec_selection} {audio_codec_selection} \"{output_file}\""
    os.system(ffmpeg_command)
    
    messagebox.showinfo(title="FFmpeg", message="FFmpeg command executed successfully!")

run_button = tk.Button(root, text="Run", command=run_ffmpeg)
run_button.grid(row=8, column=1, pady=10)

root.mainloop()
