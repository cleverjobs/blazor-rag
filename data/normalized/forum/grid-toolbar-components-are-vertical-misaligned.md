# Grid toolbar components are vertical misaligned

## Question

**Bla** asked on 17 Jun 2021

Inside the grid toolbar I have a mix of components: dropdownlist, command buttons and toogle buttons in a toggle button group. Everything works fine, the problem is that the vertical alignment of the dropdown lists and the toggle button group is different from that of the command buttons (see attached image). I tried different styles or wrapping everything in a div and setting the styles but have not been successful. Could you tell me that I should modify in order to get the buttons vertically aligned? Thanks.

## Answer

**Blazorist** answered on 17 Jun 2021

Well, I found that overriding css style k-button and set margin-top to 0 will align the buttons of the grid toolbar regardless of the type of button they are. Just add this style: <style>.k-button { margin-top: 0;
}
</style> Bye.

### Response

**Blazorist** commented on 17 Jun 2021

By the way, it would be nice if the buttons appear vertically aligned without needing this workaround.
