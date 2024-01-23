# Credits

I have to be honest, I've reached out of time, so I've made the choice to take Dockerfile and docker-compose from https://github.com/docker/awesome-compose.

So I have to credit this repository even if the license didn't mention the necessity to mention it.

# Feedback to this exercise

- Too oriented front-end.

I've spent a lot of time to deal with front-end, and most of the specification asked are about the UI (Maybe a PO could help to specify some fake case, a product should not be driven by screen). I think that if I've made my own design system it could have been done faster.


- Too much guided but I understand

You asked about a really accurate version of Ecma Script, ES2016 (ES7), actually we are at ES2024 (ES15)
There's 8 versions off, recently ES change some internal mechanism that can break the backward compatibility (default attribute are hard-undefined in the enumeration of a prototype)

Example:
```javascript
// since ES2021
class Foo {
    bar
}

// before: console.log(new Foo()) => {}
// after: console.log(new Foo()) => {bar: undefined}
```

And this little thing make a lot of break changes.

- Ask too much time to do, but it's not that hard to do

I've spent 1 hour a day on this (~7 hours) most time I was tired due to the hard way to come back home and the amount of work I have to do in my current job (I'm part of people that are like centric actually even if I try to propagate my knowledge to my mates)

If you design the exercise with a PO it could be better

- Missing some functional interest

Actually I understand that this is a technical test, but we'll work on a product into a feature team (with some tech plus asked, but I want to say it's not like tooling). It could be interesting to see if the candidate got this mind-product-vision and reflexions about the product.

Here I've worked on a tool that provide exchange rates (traders love me !)
I offer 2 functionality to my end users:
- They can refresh theirs view to get latest rates.
- They can filter on a specific rate.
=> Actually I'm asking why, why my users need a table to see rates when it could see the line that he want to see

I've made a bonus one:
- They can paginate over the table of rates to avoid any screen data overloading.
With my bonus functionality I could provide some technical improvement and functional cleaning.
I could suggest this functionnality
- They always get the most recent data
- They can paginate to get more data

Technical implementation can help to improve/optimize network I/O
- Make a function generator to go over the pagination
- Hit iteration of the function generator for "next"
- Make a new function generator for the "previous" and kill the function generator mentioned above
- etc...

There's no more functional thing in it (the scheduler is a technical implementation to provide data to end-users)

- The thing asked about the minimization & webpack are already handled by vue.js and yarn natively.
Many optimization tools are bundled into TS/VueJs/Yarn etc.

- We could dig a little bit deeper to get something fascinating to test someone.
I would be glad to help and provide a test that is programming-side-agnostic and that can help to know if a people fit to the technical level AND have this functional mind vision to challenge the needs (I'm not the best, but I would be happy to help)

Finally, I hope that you've enjoyed this projects, I know that there's missing tests, I've made component testing but with a different methodology ( I would be glad to show if you want :) )

If I've got more time I would write those integration tests on the routes of the backend and gherkin functional tests on the frontend.