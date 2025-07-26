# Telerik Animation Container appears on screen then begins animation

## Question

**Dav** asked on 24 Jun 2024

I am having a really strange issue with an animation container. For reference, this animation container appears in one half of a Splitter, and the container includes a Grid which loads data. When I prompt the animation container, with the container animation set to "SlideLeft", the container immediately appears in middle of the splitter, but then animates to the left before jumping back. The confusing part is that I have other virtually identical implementations of the animation container that do not exhibit this issue. The animation container content is provided generically through a render fragment. Showing and hiding of the container is handled through a custom "container stack" component we have written, but this is common between the working and stuttering containers. Any thoughts as to what would cause this? We are using the same parent container for multiple animation containers, although only one is shown on top at a time.

## Answer

**Tsvetomir** answered on 27 Jun 2024

Hello David, I tried to recreate the described behavior with a similar configuration as the described one. As a result, the AnimitationContainer seems to be working correctly without any positional issues. This leads me to think that I'm missing something from the actual configuration that will help me reproduce the scenario. As a next step, could you send me a REPL example that reproduces the behavior you are facing and send it back to me for inspection? This will allow me to see the behavior firsthand and offer a suitable solution. I eagerly anticipate hearing back from you. Regards, Tsvetomir Progress Telerik
