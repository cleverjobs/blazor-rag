# Async initialization of dialog when displayed

## Question

**Rob** asked on 14 Jan 2022

The dialog doesn't seem to be properly initialized in this scenario. REPL: Example

## Answer

**Hristian Stefanov** answered on 19 Jan 2022

Hi Robert, The described problem occurs because the async data comes after showing the dialog. You need to redraw the component here by using the Dialog Refresh() method. I have modified the example with the above approach. Please run and test this REPL link. Regards, Hristian Stefanov

### Response

**Haiqiang** answered on 14 Feb 2022

Hi Telerik, I have a similar async problem with Dialog, please check my scenario in this example link. In this scenario I expecting to see the dialog after 2 seconds when you press the button 'Show', so seems that Dialog doesn't like to be called asynchronously and leads to my question: is there any async-oriented call to show the Dialog or any workaround to make it work in this kind of scenario? Thanks in advance. Update: I've solved the problem by replacing the line 29 from DialogRef.Refresh() to StateHasChanged() so the UI is manually refreshed when the async Task finishes BR
