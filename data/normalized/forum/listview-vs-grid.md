# ListView vs Grid

## Question

**Sté** asked on 01 Nov 2022

Hi, Can someone gives the PROS and CONS when comparing a ListView and a Grid? Some devs here are ALWAYS using a Grid while some others go with a ListView frequently. The ones going with the Grid are barely using all the features. The rest is choosing the component based on some criterions like if it's simple use a ListView otherwise then use a Grid. The Grid seems to heavy (memory, speed, etc.) for some cases. The ones choosing the Grid absolutely all the time are saying it does the job (the argument is "I don't have to write a lot of code") why bother with the ListView. The ones going with the ListView are saying they prefer to control everything and it feels lightweight. Thanks in advance Stéphane

### Response

**Dimo** commented on 01 Nov 2022

This looks like a question for the developer community, but I will give my two cents from our point of view as a component vendor. The Grid has a predefined HTML output, which allows it to provide more built-in features with a predefined user interface. The ListView does not have a predefined HTML output, which is its major pro and con at the same time. On one hand, the developer can render anything. On the other hand, the developer needs to implement all other UI features manually (if necessary at all). If you have tabular data, it makes more sense to render it in a table, no matter if you use a Grid or a ListView. If you prefer to use a ListView with <table> tags - that's fine too.
