# EM&bull;Script &mdash; EM&#8482; Reimagined 


Welcome to **EM&bull;Script** [_ˈɛm.script_&thinsp;] &ndash; a novel programming environment targeting resource-constrained embedded systems using technology rooted in the **EM**&#8482; language.&thinsp; To increase your understanding, this site documents all aspects of the **EM&bull;Script** software platform.

<!-- imagemapper.noc.io -->

<div style="margin-bottom: -15px">
<svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1262 674">
  <image width="1262" height="674" xlink:href="/assets/splash.png"></image>
  <a xlink:href="https://www.linkedin.com/company/the-em-foundation/about/?viewAsMember=true" target="_blank">
    <rect x="6" y="500" fill="#fff" opacity="0" width="188" height="77"></rect>
  </a>
</svg>
</div>

!!! question "1 &mdash; Refresh my memory of EM&thinsp;..."

Since its inception in 2010, the focus of the [EM Programming Language](https://docs.openem.org/) has remained constant &ndash; producing "tiny code for tiny chips" where every byte of memory and &mu;Joule of energy matters when deploying low-cost, low-power embedded systems.

Having supported more than twenty 8/16/32-bit MCUs from a dozen silicon vendors, the EM language promises a _higher-level_&thinsp; programming paradigm coupled with a _higher-level_&thinsp; of runtime performance when compared with legacy C/C++ code targeting these MCUs.

As important, just a handful of EM programmers have developed thousands of EM modules re-used across a broad range of high-volume (yet proprietary) IoT applications.&thinsp;  In late 2023, [The EM Foundation](https://www.linkedin.com/company/the-em-foundation/?viewAsMember=true) &ndash; a 501(c)(3) non-profit &ndash; announced an openly available **EM-SDK**. 

!!! question "2 &mdash; So why did you create **EM&bull;Script**"

Promoting the EM SDK through [blog posts](https://blog.openem.org/) in early 2024 elicited a mixed bag of reactions &ndash; from _"cool, good luck"_&thinsp; to _"sorry, try again"_&thinsp;.&thinsp;  Despite evidence quantifying EM's performance advantage over C/C++, a new (unknown&thinsp;!!) language will set the acceptance bar rather high.

Needless to say, the effort required to sustain a handful of developers pales in comparison to promoting, sustaining, and evolving an open-source EM language for a broader community of embedded programmers.&thinsp; This realization then led to a rather radical change of course.

**Zig&bull;EM** &ndash; announced [here](https://blog.zigem.tech/post-001/) in 3Q24 &ndash; attacked the issue head-on by nominally grafting the novel concepts and constructs of EM onto _another_&thinsp; programming language.&thinsp;

!!! zig "A hidden gem"
    First released in early 2016, [Zig](https://ziglang.org/) also offers a "higher-level programming with higher-levels of performance" value proposition when compared with C/C++.&thinsp; Zig regularly earns high-marks when held up against other modern system programming languages like Go and Rust &ndash; both already targeting embedded MCUs.

    But unlike the competition, Zig offers an inherent simplicity and transparency reminiscent of C &ndash; the incumbant system programming language which some argue Zig could supplant.&thinsp; At the same time, Zig challenges many entrenched programming practices and demands that we "think differently" from the outset.

    Speaking now from personal experience:&ensp;  While not the easiest language to master, the [Ziggit forum](https://ziggit.dev/) stands apart for how it welcomes, nutures, and encourages new members to the Zig programming community

Compared with other system programming languages, however, Zig very much remains a work in progress:&ensp; a stable 1.0 release still lies years away; and language server support within popular development environments like **VS Code** remains skeletal.

Some lessons learned from the **Zig&bull;EM** experience:

<div markdown class="em-small">

{[sp,em-color-orange]&#x25CF;&ensp;} embedding EM within another programming language can afford re-use of the latter's infrastructure

{[sp,em-color-orange]&#x25CF;&ensp;} a language combo need not compromise runtime performance [time, space, power] versus legacy EM

{[sp,em-color-orange]&#x25CF;&ensp;} while code performance remains a top priority, the _quality_&thinsp; of the coding experience can't lag far behind

</div>

which then brings us then to **EM&bull;Script** &ndash; same approach, different language&thinsp;....

!!! question "3 &mdash; What makes TypeScript an ideal host"

[TypeScript](https://www.typescriptlang.org/) &ndash; younger than EM, in fact &ndash; now claims a perennial spot amongst the five most widely used programming languages.(1) The language also enjoys first-class support within **VS Code** &ndash; an environment written in TypeScript and used by a vast majority of developers.
{ .annotate }

1. see the [Stack Overflow Developer Survey](https://survey.stackoverflow.co/2024/)

The implementation of **EM&bull;Script** does leverage many of the language services and compiler APIs  delivered as part of TypeScript [TS].&thinsp; As important, a robust TS type-system enables us to capture "the essence of EM" without leaving the confines of the TypeScript language.

But perhaps the strongest reason for choosing TypeScript comes down to this insight:

!!! bulb "&ast;NOBODY&ast; regards TypeScript as a suitable language for programming resource-constrained MCUs&thinsp;!!"

Unlike other modern programming languages that have "branched out" to target embedded MCUs [MicroPython, TinyGo, and others], TypeScript has never had a bridge into the domain of low-cost, low-power embedded systems &ndash; until now, of course&thinsp;!!


!!! question "4 &mdash; Show me some **EM&bull;Script** source code"

Well, you can't call yourself a programming language if you can't do this:&ensp; :wave: :earth_americas:

```ems linenums="1" title="em.examples.basic/Ex01_HelloP"
import em from '@$$emscript'
export const $U = em.$declare('MODULE')

export function em$run() {
    printf`hello world\n`()
}
```

And to dispel any doubts, let's view the corresponding&thinsp;{[fn].em.ts} source file inside **VS Code** using our special **EM&bull;Script** extension &ndash; which flattens your learning curve through core Type&shy;Script language services like syntax highlighting, code snippets, hover help, and intellisense.

<figure markdown id="fig1">
![Image info](/assets/fig-home-1.png)
<figcaption>EM&bull;Script workspace 
</figure>

For a more realistic and compelling example, consider this "low-level" **EM&bull;Script** module which implements a bit-banged UART transmitter using a GPIO pin:

```ems linenums="1" title="em.utils/SoftUart"
import em from '@$$emscript'
export const $U = em.$declare('MODULE')

import * as Common#u from '@em.mcu/Common.em'
import * as GpioI#u from '@em.hal/GpioI.em'

export const baud_rate = $config<u32>(9_600)
export const TxPin = $proxy<GpioI#u.$I>()

const bit_time = $config<u16>()

export namespace em$meta {
    export function em$construct() {
        bit_time.$$ = Math.floor(1_000_000 / baud_rate.$$)
    }
}

export function em$startup(): void {
    TxPin.$$.makeOutput#f()
    TxPin.$$.set#f()
}

export function put#f(data: u8): void {
    const bit_cnt = 10
    var tx_byte: u16 = (data << 1) | 0x600
    const key = Common#u.GlobalInterrupts.$$.disable#f()
    for (let i = 0; i < bit_cnt; i++) {
        Common#u.UsCounter.$$.set#f(bit_time.$$)
        if (tx_byte & 0x1) {
            TxPin.$$.set#f()
        } else {
            TxPin.$$.clear#f()
        }
        tx_byte >>= 1
        Common#u.UsCounter.$$.spin#f()
    }
    TxPin.$$.set#f()
    Common#u.GlobalInterrupts.$$.restore#f(key)
}

```



!!! question "5 &mdash; How does **EM&bull;Script** optimize target firmware"

!!! question "6 &mdash; Can I start working with the **EM&bull;Script** environment"

!!! question "7 &mdash; Tell me more about the longer-term roadmap for **EM&bull;Script**"




<!--

!!! question "1 &mdash; Remind me about EM"
    To fill a void...&thinsp; While **C** remains the dominant programming language for 8&thinsp;/&thinsp;16&thinsp;/&thinsp;32-bit microcontrollers [MCUs] with limited memory and processing resources, we see opportunites for a _higher-level_ language which at the same time paves the way for _higher-levels_ of embedded system performance.

!!! question "2 &mdash; So why create **EM&bull;Script**"
    Quite simply, by reducing overall program size &ndash; a careabout for software developers working with resource-constrained MCUs.&thinsp; Reducing runtime memory requirements not only can improve program execution time, but can dramatically lower overall power consumption within the MCU as well.

    Though the EM language translator ultimately generates (portable) C/C++ code as output, a novel _configuration_ phase within the program build-flow serves as the "secret sauce" behind these performance improvements.

    A quick pass through&thinsp; [EM&thinsp;.&thinsp;optimize = WPO&thinsp;+&thinsp;ACO](//blog.openem.org/post-005/){ .em-link } &thinsp;should offer some more insights.

-->

