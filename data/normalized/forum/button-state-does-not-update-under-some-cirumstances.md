# Button state does not update under some cirumstances

## Question

**JanJan** asked on 03 Dec 2022

I have a toggle button in a child component, which gets the selected state passed as parameter. The button click invokes an eventcallback back, so the parent can update the state. When i register an method to the eventcallback of my childcomponent which also awaits a task after updating the value, the button wont change its state. I am not a native speaker, and worried i did not explain my problem good enough so i prepared an Example PS: I have also tried this with normal TelerikButtons. In that case i passed css classes which alter the background color, based on the value of IsSelected. This also won't when DoSomething() is called. UPDATE: When i use the onclick event of a span, wrapped around the TelerikButtons, everything works as expected (does not work with a span inside a button).

## Answer

**Svetoslav Dimitrov** answered on 07 Dec 2022

Hello Jan, I can see that you have introduced 10 seconds delay in the DoSomething() method. When I waited for 10 seconds the state of the ToggleButton is correctly changed. I have lowered the delay a bit - to 1 second (1000 ms) so that you can see the change quicker. Can you check this REPL link with the modified version of the code and get back to me if it works as expected for you too? Let me know if I am missing something. Regards, Svetoslav Dimitrov
