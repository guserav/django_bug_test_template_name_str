from django.test import TestCase


class MySiteTest(TestCase):
    def test_broken_template_view(self):
        response = self.client.get("/broken_template_view")
        with self.assertRaises(TypeError):  # TODO This is the broken bit
            self.assertTemplateUsed(response, "mysite/broken_template_view")

    def test_broken_render_to_string(self):
        response = self.client.get("/broken_render_to_string")
        with self.assertRaises(TypeError):  # TODO This is the broken bit
            self.assertTemplateUsed(response, "mysite/broken_render_to_string")

    def test_working_template_view(self):  # This is behaving as the above are expected to behave
        response = self.client.get("/working_template_view")
        self.assertTemplateUsed(response, "mysite/working_template_view")

    def test_a_cache_poisining(self):
        response = self.client.get("/broken_template_view")  # Calling another view that corrupts the cache for the template
        with self.assertRaises(TypeError):  # TODO This is the broken bit
            self.assertTemplateUsed(response, "mysite/broken_template_view")

        response = self.client.get("/potentially_poisoned_view")  # Now calling the normally working template which doesn't use posix path and it is also broken.
        with self.assertRaises(TypeError):  # TODO This is the broken bit
            self.assertTemplateUsed(response, "mysite/broken_template_view")
