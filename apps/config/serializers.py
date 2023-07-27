
from rest_framework import serializers

from apps.config.models import CourseInfo, Config, Article


class ConfigSerializer(serializers.ModelSerializer):
    index_image_url = serializers.SerializerMethodField(read_only=True, method_name='get_index_image_url')
    # index_image = serializers.SerializerMethodField(read_only=True, method_name='get_index_image')
    evaluation_image_url = serializers.SerializerMethodField(read_only=True, method_name='get_evaluation_image_url')
    # evaluation_image = serializers.SerializerMethodField(read_only=True, method_name='get_evaluation_image')

    def get_index_image_url(self, config):
        request = self.context.get('request')
        index_image = config.index_image
        if index_image is None:
            return ''
        try:
            if not hasattr(index_image, 'url'):
                return ''
        except ValueError:
            return ''
        return request.build_absolute_uri(index_image.url)

    def get_evaluation_image_url(self, config):
        request = self.context.get('request')
        evaluation_image = config.evaluation_image
        if evaluation_image is None:
            return ''
        try:
            if not hasattr(evaluation_image, 'url'):
                return ''
        except ValueError:
            return ''
        return request.build_absolute_uri(evaluation_image.url)

    # def get_index_image(self, config):
    #     index_image = config.index_image
    #     if index_image is None:
    #         return ''
    #     return index_image.url
    #
    # def get_evaluation_image(self, config):
    #     evaluation_image = config.evaluation_image
    #     if evaluation_image is None:
    #         return ''
    #     return evaluation_image.url

    class Meta:
        model = Config
        fields = ['index_image', 'index_image_url', 'xetong_address', 'shop_address',
                  'evaluation_image', 'evaluation_image_url']


class CourseInfoSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(read_only=True, method_name='get_image_url')

    def get_image_url(self, course_info):
        request = self.context.get('request')
        image_url = course_info.image.url
        if image_url is None:
            return ''
        return request.build_absolute_uri(image_url)

    class Meta:
        model = CourseInfo
        fields = ['title', 'url', 'image']
        # fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(read_only=True, method_name='get_image_url')

    def get_image_url(self, article):
        request = self.context.get('request')
        image_url = article.image.url
        if image_url is None:
            return ''
        return request.build_absolute_uri(image_url)

    class Meta:
        model = Article
        fields = ['title', 'description', 'image', 'a_type', 'url']
