"""Emit immutable release-site facts for direct specialized YIDL checks."""


def add_retention_facts(generated, builder, definition):
    by_name = {item.name: item for item in definition.fields}
    site_identity = 0
    check_identity = 0
    for provider in definition.retention:
        if provider.lifetime:
            continue
        for consumer in provider.consumers:
            for constructor in (
                (False, True) if by_name[consumer].field.init else (False,)
            ):
                site_id = f"Model.{consumer}.{provider.field_name}.{constructor}"
                builder.add(
                    generated.ReleaseSitesCollection,
                    generated.DataclassReleaseSite(
                        release_site_id=site_id,
                        release_owner=f"Model.{consumer}",
                        release_provider_path=by_name[
                            provider.field_name
                        ].provider_name,
                        release_identity=site_identity,
                        release_constructor=constructor,
                    ),
                )
                for name in provider.consumers:
                    builder.add(
                        generated.ReleaseChecksCollection,
                        generated.DataclassReleaseCheck(
                            release_check_id=f"{site_id}.{name}",
                            release_site_owner=site_id,
                            release_ready_path=by_name[name].ready_name,
                            release_check_identity=check_identity,
                        ),
                    )
                    check_identity += 1
                site_identity += 1
