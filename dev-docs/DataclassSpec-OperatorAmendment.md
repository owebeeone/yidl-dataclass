# Operator-accepted locality amendment

The two independent round-2 reviewers returned GO on requirements object
`0ceb048a98f9e4464366fc1abfb0827888e8fc54`. Their full reports are preserved
verbatim. Those reports assess the decorator field-name mapping then present;
they are not reviews of this subsequent amendment.

The operator explicitly rejected that mapping. Field participation belongs on
the field declaration, so deleting the field removes its policy. Class-wide
generation switches remain booleans and must not name selected fields.

The operator agreed to retain standard per-field `compare` and give transaction
write detection its own option, while preserving existing declarations. The
amended requirements spell this separate option `write_compare`, with a defined
compatibility rule for legacy `compare="value"|"identity"`. A compatibility adapter
must preserve existing write behavior without changing shared Lifecycle markers.

The operator explicitly accepted making this specification change without another
review round. This overrides the review-loop requirement to dispatch fresh
reviewers after a changed interface. No third round is run, and no reviewer GO
is claimed for these amended bytes. The requirements are operator-accepted for
progression to detailed design, not an accepted implementation or public release.

The original findings' future regression obligations remain: independent logical
inclusion and value/identity write detection, generation enabled/disabled, and the
decorator defaults table. Add old/new write-policy compatibility and conflict
diagnostics, and a field-removal locality example.

The operator also reaffirmed permission to exceed two remediation cycles for
bounded, nonarchitectural corrections. An architectural break requires a redesign
before proceeding; it must not be disguised as another superficial patch.
