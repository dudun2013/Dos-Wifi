import os
import platform
from icons.colors import *

def clean_screen():
    os.system("cls" if platform == "nt" else "clear")

def header_tools():
    print(f"""{r}*****************************************************************{rs}
{r}*{rs}                                                               {r}*{rs}
{r}*{rs}                           {c}DOS WIFI{rs}                            {r}*{rs}
{r}*{rs}                  {b}https://github.com/YogaRmdn{rs}                  {r}*{rs}
{r}*{rs}            {y}Tools that perform DOS on Wifi networks{rs}            {r}*{rs}
{r}*{rs}                      {g}Develop by Bang yog{rs}                      {r}*{rs}
{r}*{rs}                                                               {r}*{rs}
{r}*****************************************************************{rs}""")