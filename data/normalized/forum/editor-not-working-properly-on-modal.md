# Editor not working properly on Modal

## Question

**Adr** asked on 25 May 2022

Hi, I am experiencing some problem when using TelerikEditor on Modal. The editor seems a bit slow and if you press enter, it doubles the next line and when you edit a text it creates a new line on it. See example below:

### Response

**Marin Bratanov** commented on 28 May 2022

Hi Adrian, could you post a simple REPL example that showcases this issue? The following one seems to work fine for me: [https://blazorrepl.telerik.com/wcYpGWEi34lDayP030.](https://blazorrepl.telerik.com/wcYpGWEi34lDayP030.) Simplifying the scenario may also help you see if some other logic causes this - such as how parameters pass between the current and the parent component and whether some processing happens there on the content.

### Response

**Pingu** commented on 14 Aug 2022

Hi Marin, I was about to post with a very similar situation but I found this and thought a comment here would be more appropriate. I don't get the enter issue mentioned, but very slow loading I do. I've tried everything locally, and its the TelerikEditor, removing just the editor makes the window appear and load instantly, and I removed all paramters being passed down etc to isolate it. I made a repl that has a speed issue, though its faster than what I have in my actual project... but that may just be because the repl I made is just a watered down version. The issue appears to be from using all the tools, and I think the Div editmode slows it a little also. I am using both. The reply I made is: [https://blazorrepl.telerik.com/mcEMlSQw12PUQhK134](https://blazorrepl.telerik.com/mcEMlSQw12PUQhK134) Actual scenario I am using is similar, just a bit cleaner / more things in there etc ofc.

### Response

**Tsvetomir** commented on 18 Aug 2022

Hi Matthew, In general, hierarchical nesting of components might lead to a slight delay in the performance, as well as, wrapping components inside components. Therefore, putting a fully configured editor inside a window might have a slight delay due to the hierarchical nesting that the page ends up with. During my tests, the window was always opened within a second which is a negligible delay. Regarding the double adding of the rows on an Enter press, I could not replicate it either in the REPL.
