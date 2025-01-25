---
authors: [biosbob]
date: 2024-07-01
readtime: 3
---

# The EM language is dead, long live EM !!!

For the past fifteen years, the focus of the [EM Programming Language](https://docs.openem.org/) has remained constant &ndash; producing "tiny code for tiny chips" where every byte of memory and &mu;Joule of energy matters.&thinsp;  But now, I may have unwittingly come upon a *better means*&thinsp; towards this end.

<!-- more -->

<div markdown class="em-nav-arrow">

{[sp,em-float-right][&curarr;](/blog/post-002 "Announcing Zig&bull;EM v25.0.1")}

</div>

<figure style="display:none" markdown id="fig0">
![Image info](/assets/summary-001.png)
</figure>

## If you can't beat 'em,&ensp;**Zig&bull;EM**

My zeal to promote EM earlier this year blinded me to the challenges of sustaining a novel programming language for resource-constrained embedded systems.&thinsp;  Supporting just a handful of developers over the past decade pales in comparison with the effort demanded to render EM openly and freely available to the broader embedded community.

My (rhetorical) question to the community about the need to move beyond C (towards EM, of course&thinsp;!!&thinsp;) elicited a mixed bag of reactions &ndash; from *"cool, good luck"* &thinsp;to *"sorry, try again"*&thinsp;.&thinsp; But then, I received this most consequential of comments which turned on the lights for me:&nbsp;

!!! bulb "*&quot;With a language like Zig I don't think there's need for EM&quot;*"

!!! info "FULL DISCLOSURE &ndash; You don't know what you don't know"

    I pride myself on staying informed about the latest directions in programming language design and imple&shy;mentation.&thinsp;  For me, programming languages lie at the heart of Computer Science; and for me, conceiving and evolving the EM language provided a personal path to the discipline's core.

    Honestly, I'd never even *heard*&thinsp; of **Zig** when first receiving this comment several months ago.  While attending the Embedded World Conference in N&uuml;rnberg shortly thereafter, I informally polled dozens of attendees; and with the exception of my esteemed colleague [Jeremy Bennett](https://www.linkedin.com/in/jeremypbennett/none), no one had heard of the Zig programming language either.&thinsp;  Several folks did, however, know about **zigbee&reg;** &ndash; which you'd expect from this crowd. :wink:

Like EM, Zig offers higher-level programming with higher-levels of performance when compared with C; and Zig regularly earns high-marks when held up against other modern systems programming languages like Go and Rust &ndash; both already targeting embedded MCUs.

But unlike the competition, Zig offers an inherent simplicity and transparency reminiscent of C &ndash; the incumbant systems programming language which some believe Zig could supplant.

First released in early 2016, the Zig community supporting and sustaining this novel language continues to cast its net further and wider.&thinsp; Compared with Go and Rust, however, Zig very much remains a work in progress &ndash; while capturing new followers (like me) on a daily basis.

!!! tip "If you haven't already googled &quot;Zig programming language&quot;, visit [ziglang.org](https://ziglang.org/) as a starting point."

Suffice it say, far more folks have already lined up behind Zig than would ever even <u>hear</u> of the EM programming language.  To that end, I've decided to "downgrade" EM to a programming *framework* leveraging Zig as its host language &ndash; which finally leads us to **Zig&bull;EM**.

!!! abstract "It's Zig all the way down..."

    As described [here](https://blog.openem.org/post-005/), the current rendition of EM &ndash; a transpiler written in TypeScript &ndash; generates a *meta-program* (implemented in NodeJS) whose hosted execution shapes a downstream *run-time* program (implemented in C/C++); the latter then compiles into firmware targeting some resource-constrained MCU platform.

    In the case of **Zig&bull;EM**, it will use just *one* language throughout its implementation &ndash; resulting in a 10&#10005; reduction in the amount of code I'll need to maintain; I can also leverage **ZLS**, an implementation of Microsoft's Language Server Protocol which enables Zig integration with VSCode and other popular IDEs.

    And above all, you can direct all questions&thinsp;/&thinsp;comments about the Zig language to the Zig community &ndash; as will I.

As its overarching goal, the **Zig&bull;EM** framework strives to *reconstitute* the novel concepts and constructs first introduced within EM by using design-time patterns, build-time tooling, and run-time services &ndash; all leveraging the latest stable release of the Zig programming language.

## Plans are worthless&thinsp;...

*... but planning is everything*&thinsp;.(1)&nbsp;  Given our unanticipated change of course, let's set some new objectives for evolving the **Zig&bull;EM** framework through the remainder of this year:
{ .annotate }

1. General Dwight D. Eisenhower,<br>34th President of the United States

<div markdown class="em-ul em-ul-bull">

focus exclusively on supporting the [TI CC2340R5](https://www.ti.com/product/CC2340R5), which served as the initial hardware platform when EM debuted late last year; my [enthusiasm](https://blog.openem.org/post-002/#mcu-target-1-ti-cc2340) for this wireless MCU hasn't waned in the interim&thinsp;!!

create a suite of basic **Zig&bull;EM** examples &ndash; mimicking the dozen EM programs originally described [here](https://docs.openem.org/using/using-02/)&thinsp; &ndash; which would then illustrate how the framework maps EM constructs onto the Zig language

benchmark the runtime performance of **Zig&bull;EM** in terms of program size, execution time, and power consumption &ndash; using our suite of basic examples along with a Zig-based re-work of [EM&bull;Mark](https://blog.openem.org/post-006/)

push forward with **Zig&bull;EM** support for the CC2340R5's 2.4&thinsp;GHz radio &ndash; eventually re-creating the minimalist BLE stack described [here](https://blog.openem.org/post-003/) and measuring its performance against TI's legacy C code

maintain a public Git repository containing the **Zig&bull;EM** framework source code &ndash; written entirely in Zig from the ground-up, and made openly available under an unconstrained MIT license

</div>

I'll try to post regular updates on progress towards these objectives, along with some high-level tours as **Zig&bull;EM** takes shape.&thinsp;  Let's see what happens, as we do live in interesting times&thinsp;!!

## How you can get involved

<div markdown class="em-ul em-ul-check">

explore the Zig language &ndash; I highly recommend Karl Sequin's [Learning Zig](https://www.openmymind.net/learning_zig/) as a starting-point

experience the "Zen of Zig" at the [Ziggit](https://ziggit.dev/) forum &ndash; a refreshing respite from the rants at [Reddit](https://www.reddit.com/r/Zig/comments/12lrzxn/a_rant_about_programming_language_complexity_and/)

read my first [post](https://ziggit.dev/t/elevating-meta-programming-into-upstream-meta-programs/4419) about **Zig&bull;EM** to the Zig dev community  &ndash; then sign-up and send me some :heart:

</div>

{[hc]}
