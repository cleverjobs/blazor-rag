# How to reload razor component?

## Question

**HYO** asked on 24 Nov 2021

I am calling the razor component in TabStrip. If the value of the parameter changes, I want to reload the razor component with that value. As of now, the razor component is called only when the div is empty, that is, when the razor component is not called, and in other situations, it is not reloaded. I want to call the razor component using the changed data through an event. In other words, it is hoped that the contents of the razor component have changed immediately. What should I do?

### Response

**Dimo** commented on 24 Nov 2021

Hello HYOKYEONG, Just to confirm that the TabStrip does not play a role in the described scenario. The required implementation for the <Drawing /> and <Cad /> components should be the same, no matter if these components are inside a TabStrip or not. You can check the Microsoft documentation about component rendering to learn more about how to refresh a component after a parameter change.
