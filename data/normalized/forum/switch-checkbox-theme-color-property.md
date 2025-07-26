# Switch / Checkbox Theme Color property

## Question

**Ant** asked on 19 May 2024

Can we get a Switch and Checkbox theme color property similar to the rest of the components. 😀

## Answer

**Dorothy** answered on 20 May 2024

For Switches, you can set the theme color by adjusting the background color, thumb color, and track color. Here’s an example of how you might define the theme colors for a switch in your CSS or styling code: .switch {
background-color: #EFEFEF; /* Background color when switch is off */
border-radius: 16px;
padding: 2px;
}

.switch .thumb {
background-color: #007AFF; /* Thumb color when switch is on */
border-radius: 50%;
transition: transform 0.2s ease-in-out;
}

.switch .track {
background-color: #D1D1D6; /* Track color */
border-radius: 16px;
}

.switch.on .thumb {
transform: translateX(20px); /* Move thumb to the right when switch is on */
} Adjust the colors (#EFEFEF, #007AFF, and #D1D1D6) to match your overall theme. The .on class ensures that the thumb moves to the right when the switch is turned on.
