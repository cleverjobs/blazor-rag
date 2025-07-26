# Add Input Type to Menu Template

## Question

**EliEli** asked on 30 Sep 2024

How would I add an input to the template of a menu? View the following REPL, it does not accept keyboard input, but it DOES accept input if holding down shift and entering capital letters. I assume the menu is capturing keystrokes somewhere. [https://blazorrepl.telerik.com/QeEtnaFW52QfOcqb30](https://blazorrepl.telerik.com/QeEtnaFW52QfOcqb30)

## Answer

**Dimo** answered on 01 Oct 2024

Hello Eli, Wrap the <input> in an element that prevents keydown event bubbling: [https://blazorrepl.telerik.com/QIbaOPYq44Ig23hk21](https://blazorrepl.telerik.com/QIbaOPYq44Ig23hk21) <span onkeydown="event.stopPropagation()"> <input type="text" /> </span> Regards, Dimo Progress Telerik
