<change>
<file change-number-for-this-file="1">django/db/migrations/executor.py</file>
<original line-count="18" no-ellipsis="true">
<![CDATA[
class MigrationExecutor:

    # Initialization and other methods

    def apply_migration(self, state, migration, fake=False, fake_initial=False):
        """Run a migration forwards."""
        migration_recorded = False
        if self.progress_callback:
            self.progress_callback("apply_start", migration, fake)
        if not fake:
            if fake_initial:
                # Test to see if this is an already-applied initial migration
                applied, state = self.detect_soft_applied(state, migration)
                if applied:
                    fake = True
            if not fake:
                # Alright, do it normally
                with self.connection.schema_editor(atomic=migration.atomic) as schema_editor:
                    state = migration.apply(state, schema_editor)
                    self.record_migration(migration)
                    migration_recorded = True
        if not migration_recorded:
            self.record_migration(migration)
        # Report progress
        if self.progress_callback:
            self.progress_callback("apply_success", migration, fake)
        return state

    # Other methods

    def unapply_migration(self, state, migration, fake=False):
        """Run a migration backwards."""
        if self.progress_callback:
            self.progress_callback("unapply_start", migration, fake)
        if not fake:
            with self.connection.schema_editor(atomic=migration.atomic) as schema_editor:
                state = migration.unapply(state, schema_editor)
        # For replacement migrations, record individual statuses
        if migration.replaces:
            for app_label, name in migration.replaces:
                self.recorder.record_unapplied(app_label, name)
        else:
            self.recorder.record_unapplied(migration.app_label, migration.name)
        # Report progress
        if self.progress_callback:
            self.progress_callback("unapply_success", migration, fake)
        return state
]]>
</original>
<modified no-ellipsis="true">
<![CDATA[
class MigrationExecutor:

    # Initialization and other methods

    def apply_migration(self, state, migration, fake=False, fake_initial=False):
        """Run a migration forwards."""
        migration_recorded = False
        if self.progress_callback:
            self.progress_callback("apply_start", migration, fake)
        if not fake:
            if fake_initial:
                # Test to see if this is an already-applied initial migration
                applied, state = self.detect_soft_applied(state, migration)
                if applied:
                    fake = True
            if not fake:
                # Alright, do it normally
                with self.connection.schema_editor(
                    atomic=migration.atomic,
                    enforce_ddl=self.connection.features.can_rollback_ddl
                ) as schema_editor:
                    state = migration.apply(state, schema_editor)
                    self.record_migration(migration)
                    migration_recorded = True
        if not migration_recorded:
            self.record_migration(migration)
        # Report progress
        if self.progress_callback:
            self.progress_callback("apply_success", migration, fake)
        return state

    # Other methods

    def unapply_migration(self, state, migration, fake=False):
        """Run a migration backwards."""
        if self.progress_callback:
            self.progress_callback("unapply_start", migration, fake)
        if not fake:
            with self.connection.schema_editor(
                atomic=migration.atomic,
                enforce_ddl=self.connection.features.can_rollback_ddl
            ) as schema_editor:
                state = migration.unapply(state, schema_editor)
        # For replacement migrations, record individual statuses
        if migration.replaces:
            for app_label, name in migration.replaces:
                self.recorder.record_unapplied(app_label, name)
        else:
            self.recorder.record_unapplied(migration.app_label, migration.name)
        # Report progress
        if self.progress_callback:
            self.progress_callback("unapply_success", migration, fake)
        return state
]]>
</modified>
</change>

<change>
<file change-number-for-this-file="2">django/db/backends/base/features.py</file>
<original line-count="14" no-ellipsis="true">
<![CDATA[
class BaseDatabaseFeatures:
    gis_enabled = False
    allows_group_by_pk = False
    allows_group_by_selected_pks = False
    empty_fetchmany_value = []
    update_can_self_select = True

    # Does the backend distinguish between '' and None?
    interprets_empty_strings_as_nulls = False

    # Does the backend allow inserting duplicate NULL rows in a nullable
    # unique field? All core backends implement this correctly, but other
    # databases such as SQL Server do not.
    supports_nullable_unique_constraints = True

    # Does the backend allow inserting duplicate rows when a unique_together
    # constraint exists and some fields are nullable but not all of them?
]]>
</original>
<modified no-ellipsis="true">
<![CDATA[
class BaseDatabaseFeatures:
    gis_enabled = False
    allows_group_by_pk = False
    allows_group_by_selected_pks = False
    empty_fetchmany_value = []
    update_can_self_select = True

    # Does the backend distinguish between '' and None?
    interprets_empty_strings_as_nulls = False

    # Does the backend allow inserting duplicate NULL rows in a nullable
    # unique field? All core backends implement this correctly, but other
    # databases such as SQL Server do not.
    supports_nullable_unique_constraints = True

    # Can we roll back DDL in a transaction?
    can_rollback_ddl = False

    # Does the backend allow inserting duplicate rows when a unique_together
    # constraint exists and some fields are nullable but not all of them?
]]>
</modified>
</change>