import utils

__all__ = ('get_avg_cpu',)


def get_avg_cpu(instance_id):
    '''
    Units: %
    '''

    args = utils.get_metric_stats_args(utils.EC2_NAMESPACE,
                                       'CPUUtilization',
                                       ('InstanceId', instance_id))

    return utils.fetch_stats(args)
