# from django.shortcuts import render
# from .models import Question, Choice
# from .forms import QuizForm
#
#
# def quiz(request):
#     questions = Question.objects.all()
#     context = {
#         'questions': questions
#     }
#     return render(request, 'quiz/quiz.html', context)
#
#
# def submit_q(request):
#     if request.method == 'POST':
#         count = 0
#         for question_id, selected_choice_id in request.POST.items():
#             try:
#                 selected_choice = Choice.objects.get(pk=selected_choice_id)
#                 if selected_choice.is_correct:
#                     count += 1
#                     print(count)
#             except Choice.DoesNotExist:
#                 pass
#         return render(request, 'quiz/result.html', {'score': score})
