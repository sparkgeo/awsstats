import utils

__all__ = ('get_avg_cpu',
           'get_avg_read_iops',
           'get_avg_write_iops',
           'get_avg_free_memory',
           'get_avg_free_storage',
           'get_avg_swap_usage',
           'get_avg_connections',)


def get_avg_cpu(db_instance_name):
    '''
    Units: %
    '''
    dimension = ('DBInstanceIdentifier', db_instance_name)
    args = utils.get_metric_stats_args(utils.RDS_NAMESPACE,
                                       'CPUUtilization',
                                       dimension)
    return utils.fetch_stats(args)


def get_avg_read_iops(db_instance_name):
    '''
    Units: Count/Second
    '''

    dimension = ('DBInstanceIdentifier', db_instance_name)
    args = utils.get_metric_stats_args(utils.RDS_NAMESPACE,
                                       'ReadIOPS',
                                       dimension)
    return utils.fetch_stats(args)


def get_avg_write_iops(db_instance_name):
    '''
    Units: Count/Second
    '''

    dimension = ('DBInstanceIdentifier', db_instance_name)
    args = utils.get_metric_stats_args(utils.RDS_NAMESPACE,
                                       'WriteIOPS',
                                       dimension)
    return utils.fetch_stats(args)


def get_avg_free_memory(db_instance_name):
    '''
    Units: Gigabytes
    '''

    dimension = ('DBInstanceIdentifier', db_instance_name)
    args = utils.get_metric_stats_args(utils.RDS_NAMESPACE,
                                       'FreeableMemory',
                                       dimension)
    return [(a, b / 1000000000) for a, b in utils.fetch_stats(args)]


def get_avg_free_storage(db_instance_name):
    '''
    Units: Megabytes
    '''

    dimension = ('DBInstanceIdentifier', db_instance_name)
    args = utils.get_metric_stats_args(utils.RDS_NAMESPACE,
                                       'FreeStorageSpace',
                                       dimension)
    return [(a, b / 1000000) for a, b in utils.fetch_stats(args)]


def get_avg_swap_usage(db_instance_name):
    '''
    Units: Megabytes
    '''

    dimension = ('DBInstanceIdentifier', db_instance_name)
    args = utils.get_metric_stats_args(utils.RDS_NAMESPACE,
                                       'SwapUsage',
                                       dimension)
    return [(a, b / 1000000) for a, b in utils.fetch_stats(args)]


def get_avg_connections(db_instance_name):
    '''
    Units: Count
    '''

    dimension = ('DBInstanceIdentifier', db_instance_name)
    args = utils.get_metric_stats_args(utils.RDS_NAMESPACE,
                                       'DatabaseConnections',
                                       dimension)
    return utils.fetch_stats(args)
