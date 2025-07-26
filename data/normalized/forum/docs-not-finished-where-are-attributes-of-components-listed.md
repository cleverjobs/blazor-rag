# Docs not finished? Where are attributes of components listed?

## Question

**Bit** asked on 24 Oct 2019

For example, the menu component. Where are all the available attributes and events listed for this component. Yes, I see in the examples a "Data" and "orientation" attribute are used, but seems this should be explained in an "api" section for each component? I see the API Reference link but this seems like just a dump of the entire library, rather than a component-by-component reference? However, same goes for the other components as well.

## Answer

**Marin Bratanov** answered on 25 Oct 2019

Hello, This is the general way conceptual documentation (that is, those articles you see under /components, for example) and API reference are separated. Cloning the API reference causes outdated information and incomplete lists in the long run, in addition to a maintenance burden that takes time away from other, more beneficial tasks (such as creating more examples). The two must not be copies of each other, the full API reference that is taken from the codebase itself is the place to see all the available parameters and events. You can also see them in the VS Intellisense. The conceptual documentation articles are about as complete as they would be. I will not add full copies of the API reference to them, and I am considering what to do with the existing ones, especially around the grid columns, and I may remove them in favor of a few examples and links to the actual API reference. By the way, the filter field on the top left corner lets you easily find the components you seek, just start typing their name there (e.g., "TelerikGrid" or "TelerikTabStrip") and you will see the relevant articles only. Regards, Marin Bratanov
