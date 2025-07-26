# How to add HTML/ARIA attributes to Telerik components?

## Question

**Tej** asked on 19 Nov 2021

Is it possible for users to add their own HTML/ARIA attributes to Telerik components as needed? There are some elements in Telerik components that are failing Success Criterion 4.1.2, "ARIA attribute cannot be used, add a role attribute or use a different element: aria-label", because they have the aria-label attribute but they don't have the required aria-role attribute to go along with it. One example is in the grid component: [https://demos.telerik.com/blazor-ui/grid/keyboard-navigation.](https://demos.telerik.com/blazor-ui/grid/keyboard-navigation.) Demo the component using "EDIT IN TELERIK REPL" and run an axe or Accessibility Insights test on the page to see these errors on a couple of elements. One of the elements that has this error is the next/previous button for pagination: <a data-index="10" aria-label="Go to the next page" title="Go to the next page" class="k-link k-pager-nav " tabindex="-1"> <!--!--> <span class="k-icon k-i-arrow-60-right" role="presentation"> </span> <!--!--> </a> In this case, we would need to add the appropriate aria-role attribute to the <a> tag. What is the best way to add these attributes? Also, are you planning on fixing this accessibility issue across all your components?

## Answer

**Joana** answered on 24 Nov 2021

Hi Tejinder, The accessibility compliance is with high importance for our company. We have started working towards fixing the issues reported by static analyzer tools along with screen readers. Thus, our goal is to have all of our component compliant and to provide documentation resources of what is the reference accessibility specifications, what are the tools used for testing and fully accessible pages for testing. Regarding the reported violations in this thread with the Pager component - they are going to be fixed with the upcoming release in early December. We have a
