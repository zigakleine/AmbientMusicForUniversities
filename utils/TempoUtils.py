class TempoUtils:

    @classmethod
    def get_bps_from_bpm(cls, bpm):
        return bpm / 60

    @classmethod
    def get_bpm_from_bps(cls, bps):
        return bps * 60

    @classmethod
    def get_note_duration_from_bpm_seconds(cls, note_duration, bpm):
        # beats per minute
        quarter_note_duration = 60 / bpm

        if note_duration == "quarter_note":
            return quarter_note_duration

        elif note_duration == "eigth_note":
            return quarter_note_duration / 2


