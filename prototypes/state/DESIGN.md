---
name: Civic Intelligence System
colors:
  surface: '#f8f9fb'
  surface-dim: '#d9dadc'
  surface-bright: '#f8f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f4f6'
  surface-container: '#edeef0'
  surface-container-high: '#e7e8ea'
  surface-container-highest: '#e1e2e4'
  on-surface: '#191c1e'
  on-surface-variant: '#594046'
  inverse-surface: '#2e3132'
  inverse-on-surface: '#f0f1f3'
  outline: '#8d6f76'
  outline-variant: '#e0bec5'
  surface-tint: '#b9045e'
  primary: '#b9045e'
  on-primary: '#ffffff'
  primary-container: '#ff4b91'
  on-primary-container: '#5a002a'
  inverse-primary: '#ffb1c6'
  secondary: '#575e70'
  on-secondary: '#ffffff'
  secondary-container: '#d9dff5'
  on-secondary-container: '#5c6274'
  tertiary: '#006e11'
  on-tertiary: '#ffffff'
  tertiary-container: '#00a920'
  on-tertiary-container: '#003304'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffd9e1'
  primary-fixed-dim: '#ffb1c6'
  on-primary-fixed: '#3f001b'
  on-primary-fixed-variant: '#8e0046'
  secondary-fixed: '#dce2f7'
  secondary-fixed-dim: '#c0c6db'
  on-secondary-fixed: '#141b2b'
  on-secondary-fixed-variant: '#404758'
  tertiary-fixed: '#75ff6d'
  tertiary-fixed-dim: '#57e154'
  on-tertiary-fixed: '#002202'
  on-tertiary-fixed-variant: '#00530a'
  background: '#f8f9fb'
  on-background: '#191c1e'
  surface-variant: '#e1e2e4'
  status-escalated: '#E11D48'
  status-reviewing: '#F59E0B'
  status-action: '#10B981'
  data-surface: '#FFFFFF'
  text-muted: '#6B7280'
typography:
  headline-xl:
    fontFamily: Hanken Grotesk
    fontSize: 40px
    fontWeight: '700'
    lineHeight: 48px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Hanken Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  headline-md:
    fontFamily: Hanken Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  data-numeral:
    fontFamily: Hanken Grotesk
    fontSize: 28px
    fontWeight: '700'
    lineHeight: 32px
  label-sm:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  grid-columns: '4'
  gutter: 1.5rem
  margin-desktop: 2rem
  margin-mobile: 1rem
  card-padding: 1.25rem
---

## Brand & Style

The brand personality is **authoritative yet accessible**. It functions as a bridge between complex civic data and actionable public discourse. The visual direction evolves the previous identity by moving from a social-first aesthetic to a **Corporate Modern** framework with high-density data visualizations.

The design should evoke feelings of **clarity, progress, and impartiality**. It utilizes heavy whitespace to manage information density, ensuring that complex dashboards feel calm rather than overwhelming. The hallmark of this design system is the "Soft-Data" approach: utilizing the warmth of the pink/white palette to humanize quantitative civic intelligence.

## Colors

The palette is anchored by a high-vibrancy primary pink (`#FF4B91`) used sparingly for critical call-to-actions and brand presence. The primary background is off-white to reduce eye strain during long-form data analysis.

For civic intelligence status indicators, we use a custom semantic set:
- **Escalated:** A deep rose-red, signaling urgency without triggering alarm.
- **Reviewing:** A warm amber, indicating active processing.
- **Action Taken:** A calm emerald, signifying resolution and progress.

Neutral tones prioritize a cool-gray scale to maintain a professional, tech-forward feel.

## Typography

This design system utilizes a three-font strategy to distinguish between narrative and data:
- **Hanken Grotesk** is used for headlines and large data numerals. Its sharp, contemporary geometry provides the "intelligence" aesthetic.
- **Inter** handles all body copy and descriptions, chosen for its exceptional legibility in dense layouts.
- **Manrope** is reserved for labels, metadata, and status tags, providing a balanced, technical feel for micro-copy.

Hierarchy is enforced through strict weight contrast rather than just size, ensuring that even in high-density grids, the user's eye is led to primary insights first.

## Layout & Spacing

The layout is built on a **12-column underlying grid**, which reflows into a **4-column dashboard layout** for primary content modules. 

- **Dashboard View:** Content cards typically span 1 or 2 columns of the 4-column layout.
- **Information Density:** We utilize a "tight but airy" rhythm. Padding inside cards is generous (`1.25rem`), but the gutters between cards are kept at a standard `1.5rem` to maximize the amount of visible data on a single screen.
- **Breakpoints:**
  - **Desktop (1280px+):** Full 4-column dashboard.
  - **Tablet (768px - 1279px):** 2-column stacked layout.
  - **Mobile (<768px):** Single-column vertical scroll with reduced horizontal margins.

## Elevation & Depth

To maintain a clean and structured look, this design system avoids heavy shadows. Instead, it uses **Tonal Layering** and **Low-contrast Outlines**:

- **Surface Level 0:** The main application background (`#F3F4F6`).
- **Surface Level 1 (Cards):** Pure white background (`#FFFFFF`) with a subtle `1px` border in a slightly darker neutral tint.
- **Active State:** A very soft, large-radius ambient shadow is only used when a card is hovered or focused, lifting it visually to indicate interactivity.
- **Depth through Color:** Sidebar and navigation elements use semi-transparent blurs (glassmorphism) over the primary brand colors to create a sense of persistent context.

## Shapes

The shape language is **Rounded**, following the heritage of the original brand but refined for a professional context. 

- **Cards & Modules:** Use a `1rem` (16px) corner radius to soften the high-density data.
- **Buttons & Tags:** Utilize a slightly more aggressive `0.5rem` radius or full pill-shape for interactive elements to distinguish them from static content containers.
- **Form Inputs:** Match the card roundedness at `0.5rem` to maintain a cohesive structural language.

## Components

### Buttons
Primary buttons use the brand pink with white text. Secondary buttons use a ghost style (outline only) with the primary color text. All buttons have a height of 44px for accessibility and professional presence.

### Data Cards
Cards are the primary container. They must include a clear header area with a label (Manrope) and a value (Hanken Grotesk). The footer of a card is reserved for "Trend Indicators" or "Status Tags."

### Status Tags
Small, pill-shaped indicators using the `named_colors`. Backgrounds are 15% opacity of the status color, with text at 100% opacity for maximum legibility and a "calm" appearance.

### Input Fields
Inputs are minimal, featuring a `1px` border that transitions to the brand pink on focus. Labels always sit above the input in `label-sm` typography.

### Progress & Trends
Sparklines and trend bars should use the `Action Taken` green for positive growth and `Escalated` red for negative trends, maintaining the "Professional Civic" tonal balance.