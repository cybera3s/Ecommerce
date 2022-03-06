from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from .forms import CommentCreateForm


class CommentCreateView(View):
    form_class = CommentCreateForm

    # @method_decorator(login_required)
    # def post(self, request):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         new_comment = form.save(commit=False)
    #         new_comment.user = request.user
    #         new_comment.post = self.post_instance
    #         new_comment.save()
            # messages.success(request, 'your comment added', 'success')
            # return redirect('home:post_detail', self.post_instance.id, self.post_instance.slug)
